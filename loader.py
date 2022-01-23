import cv2
import os


arr = os.listdir('/home/siddhartha/Siddhartha/Reveal-Media/Shufflefacenet_cosface/dataloader/lfwdata/lfw')


def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images

lfwd_dir = '/home/siddhartha/Siddhartha/Reveal-Media/Shufflefacenet_cosface/dataloader/lfwdata/lfw'
for i in arr:
    X = load_images_from_folder(os.path.join(lfwd_dir,i))
    print(len(X))
