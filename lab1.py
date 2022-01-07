import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from skimage.io import imread, imshow, imsave
from skimage.color import rgb2hsv, hsv2rgb
from skimage.filters import rank as skr
from skimage.morphology import disk

# -- Your code here -- #
def place_watermark(img_path, watermark_path, pos_x, pos_y, save_path=None):
    img = imread(img_path)
    watermark = imread(watermark_path)

    size_y, size_x = watermark.shape

    if pos_y + size_y > img.shape[0] or pos_x + size_x > img.shape[1] or pos_x < 0 or pos_y < 0:
        raise Exception("Position out of bounds")

    img = rgb2hsv(img)

    val = img[pos_y:pos_y + size_y, pos_x:pos_x + size_x, 2]

    avg = np.average(val)  # check if the image should be darker or lighter
    if avg >= 0.5:
        diff = -0.4
    else:
        diff = 0.4

    for i in range(size_y):
        for j in range(size_x):
            if watermark[i, j] == 255:
                val = img[pos_y + i][pos_x + j][2]
                val += diff
                if val < 0:
                    val = 0
                elif val > 1:
                    val = 1

                img[pos_y + i][pos_x + j][2] = val

    img = hsv2rgb(img)

    if save_path != None:
        imsave(save_path, img)

    return img


img = place_watermark("etretat.jpg", "watermark.png", 700, 300, "test.jpg")

plt.figure()
imshow(img, interpolation='nearest')
