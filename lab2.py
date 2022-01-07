import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from skimage.io import imread, imshow, imsave
from skimage.morphology import disk
from skimage.color import rgb2ycbcr, ycbcr2rgb
from skimage.filters.rank import mean


# -- Your code here -- #
def noise_reduction(im):
    # reduce noise by using a median filter with a disk kernel
    kernel = disk(4)
    return mean(im, kernel)


def stretch_contrast(im):
    im_ycc = rgb2ycbcr(im)
    y_chan = im_ycc[:, :, 0]

    y_min, y_max = np.amin(y_chan), np.amax(y_chan)
    print(y_min, y_max)
    shape = im_ycc.shape
    res_y_chan = np.zeros((shape[0], shape[1]), dtype=np.uint8)

    for y in range(shape[0]):
        for x in range(shape[1]):
            res_y_chan[y, x] = np.uint8((219 * (y_chan[y, x] - y_min) / (y_max - y_min)) + 16)

    im_ycc[:, :, 0] = res_y_chan

    return ycbcr2rgb(im_ycc)


def enhance(im, noise_red=False, fix_contrast=False):
    if noise_red:
        im = noise_reduction(im)
    if fix_contrast:
        im = stretch_contrast(im)
    return im


im = imread("low_cont.jpg")
plt.figure()
plt.imshow(im)
plt.show()

im = enhance(im, fix_contrast=True)

plt.figure()
plt.imshow(im)
plt.show()
imsave("test_save.jpg", im)