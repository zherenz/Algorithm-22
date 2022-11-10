import numpy as np

# W = input size; F = kernel size; P = padding; S = stride; N = output size
# N = (W - F + 2 * P) // S + 1

# padding the image & convolution
def filter_image_vec(image, h_filter):
    h_row, h_col = h_filter.shape
    row_padding = int(np.floor(h_row/2))
    col_padding = int(np.floor(h_col/2))
    image_pad = np.pad(image, ((row_padding, row_padding), (col_padding, col_padding)),'constant', constant_values = (0, 0))
    windows = []
    
    # Perform convolution on the padded image.
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            window = image_pad[i: i + h_filter.shape[0], j : j + h_filter.shape[1]]
            windows.append(window.reshape(-1, 1))
    image_to_convolve = windows
    image_filter = h_filter.reshape(1, -1)
    image_output = np.reshape(np.dot(image_filter, image_to_convolve),(image.shape[0],image.shape[1]))
    
    return image_output


def convolution2d(image, kernel, stride, padding):
    # Cross Correlation
    kernel = np.flipud(np.fliplr(kernel))
    # Pad
    image = np.pad(image, [(padding, padding), (padding, padding)], mode='constant', constant_values=0)

    kernel_height, kernel_width = kernel.shape
    padded_height, padded_width = image.shape

    output_height = (padded_height - kernel_height) // stride + 1
    output_width = (padded_width - kernel_width) // stride + 1

    new_image = np.zeros((output_height, output_width)).astype(np.float32)

    for y in range(0, output_height):
        for x in range(0, output_width):
            new_image[y][x] = np.sum(image[y * stride:y * stride + kernel_height, x * stride:x * stride + kernel_width] * kernel).astype(np.float32)
    return new_image
