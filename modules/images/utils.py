import cv2
import numpy as np

def resize_image(img, size=(20,20)):

    h, w = img.shape[:2]
    
    if h == w: 
        return cv2.resize(img, size, cv2.INTER_AREA)

    dif = h if h > w else w


    if dif > (size[0] + size[1]):
        interpolation = cv2.INTER_AREA
    else:
        interpolation = cv2.INTER_CUBIC

    x_pos = (dif - w)//2
    y_pos = (dif - h)//2

    mask = np.zeros((dif, dif), dtype=img.dtype)
    mask[y_pos:y_pos+h, x_pos:x_pos+w] = img[:h, :w]

    return cv2.resize(mask, size, interpolation)