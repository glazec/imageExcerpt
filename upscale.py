import colorgram
from skimage import data, color
from skimage.transform import rescale, resize, downscale_local_mean
from skimage import io
from skimage import img_as_ubyte
from PIL import Image
import os

image = io.imread('hues.png')
x = image.shape[0]
y = image.shape[1]
new_shape = (600, 500, image.shape[2])
image_rescaled = resize(image, new_shape, preserve_range=True)
io.imsave('image.png', image_rescaled)
