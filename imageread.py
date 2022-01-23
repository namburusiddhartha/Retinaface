import os
import cv2

arr = os.listdir('/home/siddhartha/Siddhartha/Reveal-Media/Shufflefacenet_cosface/dataloader/lfwdata/lfw')
lfwd_dir = '/home/siddhartha/Siddhartha/Reveal-Media/Shufflefacenet_cosface/dataloader/lfwdata/lfw'
asp = []
for x in arr:
    imgpth = ""
    folder = os.path.join(lfwd_dir,x)
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            imgpth = os.path.join(folder,filename)

        image_path = imgpth
        img_raw = cv2.imread(image_path, cv2.IMREAD_COLOR)
        h,w,_ = img_raw.shape
        asp.append(h/w)
A = sum(asp)/len(asp)
print(A)
