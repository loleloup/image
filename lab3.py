import numpy as np
import matplotlib.pyplot as plt
from skimage.filters.rank import mean
from skimage.morphology import disk
from skimage.io import imread, imshow, imsave



# Your code here
# histogram based segmentation as seen in class

def segment(im):
    treshold_min = 165
    treshold_max = 246
    im = mean(im[:, :, 0], disk(4))
    im_out = np.zeros(im.shape)
    for y in range(im.shape[0]):
        for x in range(im.shape[1]):
            if treshold_min < im[y, x] < treshold_max:
                im_out[y, x] = True
            else:
                im_out[y, x] = False

    return im_out


im = imread('mri_brain.jpg')
imshow(im)
print(im.shape)

im_out = segment(im)
print(im_out.sum() * 0.115 * 0.115, "square cm")
plt.figure()
imshow(im_out)
imsave("contour.png", im_out)
plt.figure()
imshow(im)
