def measure(img, txt, thres=''):
    import numpy as np
    import cv2
    from PIL import Image
    import pandas as pd

    # Load image as grayscale, count pixel under thres value 
#     img_file = img_path # SEM image file
    df = pd.DataFrame(txt)
    df = df.astype({0:'int'})
    for raw in range(len(df)):
        if df.loc[raw,0]==1:
            df =df.drop(raw, axis=0)
    txt = df.to_numpy()[:,1:]

    face_list = []
    for d in range(len(txt)):
        obj = txt[d]
        for x in [0,2]:
            obj[x] = obj[x]*(img.size)[0]
        for y in [1,3]:
            obj[y] = obj[y]*(img.size)[1]
        face = (obj[2])*(obj[3])
        face_list.append(face)
    face_pixel = sum(face_list)/len(face_list)
    face_pixel = face_pixel*(320/640)*(320/640)
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
    ratio = count / (w * h)
    road_pixel = (w*h)*ratio
    
    area = road_pixel * ((0.157 * 0.228)/face_pixel)

#     print(f"Area: {area} square meters")
    
    return area