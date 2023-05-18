#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def area_segmentation(X_train, y_train, X_val, y_val, X_test, y_test, classes=['road','pavement'],
                     BACKBONE = 'efficientnetb3', BATCH_SIZE = 4, LR = 0.0001, EPOCHS = 40):
    
    import cv2
    import keras
    import numpy as np
    import matplotlib.pyplot as plt
    from PIL import Image
    from sklearn.model_selection import train_test_split
    import albumentations as A
    import os
    
    import segmentation_models as sm
#     from pre_aug.preprocessing import Dataset, test_Dataset
#     from pre_aug.augmentation import get_training_augmentation, get_validation_augmentation, get_preprocessing

    # preprocessing
    def visualize(**images):
        """PLot images in one row."""
        n = len(images)
        plt.figure(figsize=(16, 5))
        for i, (name, image) in enumerate(images.items()):
            plt.subplot(1, n, i + 1)
            plt.xticks([])
            plt.yticks([])
            plt.title(' '.join(name.split('_')).title())
            plt.imshow(image)
        plt.show()

    # helper function for data visualization    
    def denormalize(x):
        """Scale image to range 0..1 for correct plot"""
        x_max = np.percentile(x, 98)
        x_min = np.percentile(x, 2)    
        x = (x - x_min) / (x_max - x_min)
        x = x.clip(0, 1)
        return x


    # classes for data loading and preprocessing
    class Dataset:
        """CamVid Dataset. Read images, apply augmentation and preprocessing transformations.

        Args:
            images_dir (str): path to images folder
            masks_dir (str): path to segmentation masks folder
            class_values (list): values of classes to extract from segmentation mask
            augmentation (albumentations.Compose): data transfromation pipeline 
                (e.g. flip, scale, etc.)
            preprocessing (albumentations.Compose): data preprocessing 
                (e.g. noralization, shape manipulation, etc.)

        """

        CLASSES = ['sky', 'building', 'pole', 'road', 'pavement', 
                   'tree', 'signsymbol', 'fence', 'car', 
                   'pedestrian', 'bicyclist', 'unlabelled']

        def __init__(
                self, 
                images_dir, 
                masks_dir, 
                classes=None, 
                augmentation=None, 
                preprocessing=None,
        ):
            self.ids = os.listdir(images_dir)
            self.images_fps = [os.path.join(images_dir, image_id) for image_id in self.ids]
            self.masks_fps = [os.path.join(masks_dir, image_id) for image_id in self.ids]

            # convert str names to class values on masks
            self.class_values = [self.CLASSES.index(cls.lower()) for cls in classes]

            self.augmentation = augmentation
            self.preprocessing = preprocessing

        def __getitem__(self, i):

            # read data
            image = cv2.imread(self.images_fps[i])
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            mask = cv2.imread(self.masks_fps[i], 0)

            # extract certain classes from mask (e.g. cars)
            masks = [(mask == v) for v in self.class_values]
            mask = np.stack(masks, axis=-1).astype('float')

            # add background if mask is not binary
            if mask.shape[-1] != 1:
                background = 1 - mask.sum(axis=-1, keepdims=True)
                mask = np.concatenate((mask, background), axis=-1)

            # apply augmentations
            if self.augmentation:
                sample = self.augmentation(image=image, mask=mask)
                image, mask = sample['image'], sample['mask']

            # apply preprocessing
            if self.preprocessing:
                sample = self.preprocessing(image=image, mask=mask)
                image, mask = sample['image'], sample['mask']

            return image, mask

        def __len__(self):
            return len(self.ids)

    class predict_Dataset:

        def __init__(
                self, 
                images,
                augmentation=None, 
                preprocessing=None,
        ):
#             self.ids = os.listdir(images_dir)
#             self.images_fps = [os.path.join(images_dir, image_id) for image_id in self.ids]
            self.images = images

            # convert str names to class values on masks
            self.augmentation = augmentation
            self.preprocessing = preprocessing

        def __getitem__(self, i):

            # read data
    #         image = cv2.imread(self.images_fps[i])
            image = cv2.cvtColor(self.images, cv2.COLOR_BGR2RGB)

            # apply augmentations
            if self.augmentation:
                sample = self.augmentation(image=image)
                image = sample['image']

            # apply preprocessing
            if self.preprocessing:
                sample = self.preprocessing(image=image)
                image = sample['image']

            return image

        def __len__(self):
            return len(self.ids)


    class Dataloder(keras.utils.Sequence):
        """Load data from dataset and form batches

        Args:
            dataset: instance of Dataset class for image loading and preprocessing.
            batch_size: Integet number of images in batch.
            shuffle: Boolean, if `True` shuffle image indexes each epoch.
        """

        def __init__(self, dataset, batch_size=1, shuffle=False):
            self.dataset = dataset
            self.batch_size = batch_size
            self.shuffle = shuffle
            self.indexes = np.arange(len(dataset))

            self.on_epoch_end()

        def __getitem__(self, i):

            # collect batch data
            start = i * self.batch_size
            stop = (i + 1) * self.batch_size
            data = []
            for j in range(start, stop):
                data.append(self.dataset[j])

            # transpose list of lists
            batch = [np.stack(samples, axis=0) for samples in zip(*data)]

            return batch

        def __len__(self):
            """Denotes the number of batches per epoch"""
            return len(self.indexes) // self.batch_size

        def on_epoch_end(self):
            """Callback function to shuffle indexes each epoch"""
            if self.shuffle:
                self.indexes = np.random.permutation(self.indexes)   
                
    # augmentation
    def round_clip_0_1(x, **kwargs):
        return x.round().clip(0, 1)

    # define heavy augmentations
    def get_training_augmentation():
        train_transform = [

            A.HorizontalFlip(p=0.5),

            A.ShiftScaleRotate(scale_limit=0.5, rotate_limit=0, shift_limit=0.1, p=1, border_mode=0),

            A.PadIfNeeded(min_height=320, min_width=320, always_apply=True, border_mode=0),
            A.RandomCrop(height=320, width=320, always_apply=True),

            A.GaussNoise(p=0.2),
            A.Perspective(p=0.5),

            A.OneOf(
                [
                    A.CLAHE(p=1),
                    A.RandomBrightness(p=1),
                    A.RandomGamma(p=1),
                ],
                p=0.9,
            ),

            A.OneOf(
                [
                    A.Sharpen(p=1),
                    A.Blur(blur_limit=3, p=1),
                    A.MotionBlur(blur_limit=3, p=1),
                ],
                p=0.9,
            ),

            A.OneOf(
                [
                    A.RandomContrast(p=1),
                    A.HueSaturationValue(p=1),
                ],
                p=0.9,
            ),
            A.Lambda(mask=round_clip_0_1)
        ]
        return A.Compose(train_transform)


    def get_validation_augmentation():
        """Add paddings to make image shape divisible by 32"""
        test_transform = [
            A.PadIfNeeded(384, 480)
        ]
        return A.Compose(test_transform)

    def get_preprocessing(preprocessing_fn):
        """Construct preprocessing transform

        Args:
            preprocessing_fn (callbale): data normalization function 
                (can be specific for each pretrained neural network)
        Return:
            transform: albumentations.Compose

        """

        _transform = [
            A.Lambda(image=preprocessing_fn),
        ]
        return A.Compose(_transform)
    
    # train
    
    def ds_generate(X_train, y_train, X_val, y_val, X_test, y_test, BACKBONE = BACKBONE,Classes=classes):
        
        preprocess_input = sm.get_preprocessing(BACKBONE)
        
        train_dataset = Dataset(
            X_train, 
            y_train, 
            classes=Classes, 
            augmentation=get_training_augmentation(),
            preprocessing=get_preprocessing(preprocess_input))

        valid_dataset = Dataset(
            X_val, 
            y_val, 
            classes=Classes, 
            augmentation=get_validation_augmentation(),
            preprocessing=get_preprocessing(preprocess_input))
        
        test_dataset = Dataset(
            X_test, 
            y_test,
            classes=Classes, 
            augmentation=get_validation_augmentation(),
            preprocessing=get_preprocessing(preprocess_input))
        
        train_dataloader = Dataloder(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
        valid_dataloader = Dataloder(valid_dataset, batch_size=1, shuffle=False)
        test_dataloader = Dataloder(test_dataset, batch_size=1, shuffle=False)
        
        return train_dataloader, valid_dataloader, test_dataloader
        
        
    def train(train_dataloader, valid_dataloader, test_dataloader, BACKBONE = BACKBONE,
              Classes=classes, BATCH_SIZE = BATCH_SIZE, LR = LR, EPOCHS = EPOCHS):

        # define network parameters
        n_classes = 1 if len(Classes) == 1 else (len(Classes) + 1)  # case for binary and multiclass segmentation
        activation = 'sigmoid' if n_classes == 1 else 'softmax'

        #create model
        model = sm.Unet(BACKBONE, classes=n_classes, activation=activation)
        
        # define optomizer
        optim = keras.optimizers.Adam(LR)

        # Segmentation models losses can be combined together by '+' and scaled by integer or float factor
        dice_loss = sm.losses.DiceLoss(class_weights=np.array([1, 2, 0.5]))
        focal_loss = sm.losses.BinaryFocalLoss() if n_classes == 1 else sm.losses.CategoricalFocalLoss()
        total_loss = dice_loss + (1 * focal_loss)

        # metrics = [sm.metrics.IOUScore(threshold=0.5), sm.metrics.FScore(threshold=0.5)]
        metrics = [sm.metrics.IOUScore(threshold=0.5), sm.metrics.FScore(threshold=0.5)]

        # compile keras model with defined optimozer, loss and metrics
        model.compile(optim, total_loss, metrics)
        
        callbacks = [
            keras.callbacks.ModelCheckpoint('./best_model_segmentation.h5', save_weights_only=True, save_best_only=True, mode='min'),
            keras.callbacks.ReduceLROnPlateau()]
#         keras.callbacks.EarlyStopping(monitor='val_loss', patience=5)
        
        assert train_dataloader[0][0].shape == (BATCH_SIZE, 320, 320, 3)
        assert train_dataloader[0][1].shape == (BATCH_SIZE, 320, 320, n_classes)
        
        history = model.fit_generator(
            train_dataloader,
            steps_per_epoch=len(train_dataloader),
            epochs=EPOCHS,
            callbacks=callbacks,
            validation_data=valid_dataloader,
            validation_steps=len(valid_dataloader))
        
        model.load_weights('best_model_segmentation.h5') 
        
        scores = model.evaluate_generator(test_dataloader)

        print("Loss: {:.5}".format(scores[0]))
        for metric, value in zip(metrics, scores[1:]):
            print("mean {}: {:.5}".format(metric.__name__, value))
            
    train_dataloader, valid_dataloader, test_dataloader = ds_generate(X_train, y_train, X_val, y_val, X_test, y_test
                                                                      , BACKBONE = BACKBONE,Classes=classes)
    train(train_dataloader, valid_dataloader, test_dataloader, BACKBONE = BACKBONE,
          Classes=classes, BATCH_SIZE = BATCH_SIZE, LR = LR, EPOCHS = EPOCHS)

