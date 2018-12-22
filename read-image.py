from skimage import io
import numpy as np

if __name__ == '__main__':
    image_orgial = io.imread('1.jpg')
    io.imshow(image_orgial)
    io.show()
    print(image_orgial)
    image_orgial = np.asarray(image_orgial)
    print(image_orgial.shape)
