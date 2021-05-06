import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse


def convolution(img, kernel, verbose = False):
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

    for row in range(img_row):
        for col in range(img_col):
            # Dot product of the filter and the image.
            filtered = padded_img[
                row: row + kernel_row,
                col: col + kernel_col
            ]
            # Sum of the values of the dot product for each position.
            output[row, col] = np.sum(kernel * filtered)

    # Saves the result of the filter.
    cv2.imwrite("output_image.jpg", output)

    # If display is defined, it will show the result.
    if verbose:
        plt.imshow(img, cmap='gray')
        plt.title("Image")
        plt.show()

        plt.imshow(padded_img, cmap='gray')
        plt.title("Padded Image")
        plt.show()

        plt.imshow(output, cmap='gray')
        plt.title("Output Image using {}X{} Kernel".format(
            kernel_row, kernel_col))
        plt.show()

    # Returns the output matrix.
    return output


if __name__ == '__main__':
	# Takes the arguments for usage.
	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--image", required=True, help="Path to the image")
	args = vars(ap.parse_args())
	# use open cv 2 to change the image into an array of numbers
	image = cv2.imread(args["image"])

	# Filters / Kernel
	#Edge Detection Kernel
    edge_detection = np.array([
		[-1, -1, -1],
		[-1,  8, -1],
		[-1, -1, -1]
		])
    #Gaussian Blur Kernel
    gaussian_blur = np.array([
        [0,  0,   0,   5,   0,  0, 0],
        [0,  5,  18,  32,  18,  5, 0],
        [0, 18,  64, 100,  64, 18, 0],
        [5, 32, 100, 100, 100, 32, 5],
        [0, 18,  64, 100,  64, 18, 0],
        [0,  5,  18,  32,  18,  5, 0],
        [0,  0,   0,   5,   0,  0, 0]
    ])
image_gb = convolution(image, gaussian_blur, True)