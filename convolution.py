import cv2
import numpy as np

def convolution(img, kernel):
    # Converts from a 3 channel image to a 2-D array in grayscale.
    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite("greyscale_image.jpg", img)

    # Gets the dimensions of the matrices of the image and the kernel.
    img_row, img_col = img.shape
    kernel_row, kernel_col = kernel.shape

    # Defines the size of padding and the padded image to work with.
    padding = np.array([int((i - 1) / 2) for i in kernel.shape])
    padded_img = np.zeros(padding*2+img.shape)
    padded_img[padding[0]:-padding[0], padding[1]:-padding[1]] = img

    # Defines empty 2-D matrix of the size of the image as output matrix.
    output = np.zeros(img.shape)

    # Outputs matrices sizes for comprobation.
    print("Original : {}, {}".format(img_row, img_col))
    print("Kernel : {}, {}".format(kernel_row, kernel_col))
    print("Padding : {}, {}".format(padding[0], padding[1]))
    print("Padded Image : {}, {}".format(padded_img.shape[0], padded_img.shape[1]))
    print("Output : {}, {}".format(output.shape[0], output.shape[1]))

    # Returns the output matrix.
    return output


if __name__ == '__main__':
    image = cv2.imread("Testing.jpg")
    kernel = np.array([
        [1/9, 1/9, 1/9],
        [1/9, 1/9, 1/9],
        [1/9, 1/9, 1/9]
    ])

    imgage = convolution(image, kernel)
