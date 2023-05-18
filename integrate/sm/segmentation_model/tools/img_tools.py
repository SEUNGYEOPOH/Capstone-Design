def measure(img,thres='', dpi=99.9998):
    import numpy as np
    import cv2
    from PIL import Image

    # Load image as grayscale, count pixel under thres value 
#     img_file = img_path # SEM image file
        
#     img = Image.open(img_file)
    igs = img.convert('L') # image grayscale, (R,G,B)->(wb,wb,wb)
    w, h = igs.size
    # igs.save('sem_test_gs.png')

    y=np.asarray(igs.getdata(),dtype=np.uint8).reshape((h, w))
    y = y - np.amin(y) # shift values down to 0 
    
    imax = np.amax(y)
    imin = np.amin(y) # set to 0
    thres10 = int((imax-imin)/10)

    # threshold value for black
    if thres == '':
        thres = thres10
        
    y2 = y[np.where(y > thres)] # slice array and count 
    count = y2.size

    # Calculate crack percentage
    percentage = count / (w * h) * 100
    
    area = ((w*h)*percentage)/(dpi*39.37)**2

#     print(f"Area: {area} square meters")
    
    return area