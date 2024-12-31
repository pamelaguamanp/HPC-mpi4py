import numpy as np
from mpi4py import MPI
from scipy.ndimage import convolve
from scipy.datasets import face  # Updated to use scipy.datasets
from PIL import Image  # To save images

# MPI Initialization
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Load the test image
image = face()
global_shape = image.shape
local_shape = global_shape[0] // size


# Divide the image among processes
local_start = rank * local_shape
local_end = (rank + 1) * local_shape
local_image = image[local_start:local_end]

# Define convolution kernels
kernel_sizes = {'red': 11, 'green': 7, 'blue': 3}
colors = ('red', 'green', 'blue')

if rank < len(colors):  # Processes for predefined colors
    color = colors[rank]
    kernel_size = kernel_sizes[color]
else:  # Extra processes use random colors and kernels
    color = f"random_{rank}"
    kernel_size = np.random.randint(3, 12)

# Apply convolution if a color is assigned
if color is not None:
    kernel = np.ones((kernel_size, kernel_size)) / kernel_size**2
    local_result = np.zeros_like(local_image)

    for i in range(local_image.shape[2]):  # Iterate over RGB channels
        local_result[:, :, i] = convolve(local_image[:, :, i], kernel)
else:
    local_result = np.zeros_like(local_image)

# Gather results
result = None
if rank == 0:
    result = np.zeros_like(image)

comm.Gather(local_result, result, root=0)

# Save the original and processed images on the root process
if rank == 0:
    # Save the original image
    original_img = Image.fromarray(image.astype(np.uint8))
    original_img.save('original_image.jpg')
    print("Original image saved as 'original_image.jpg'")

    # Save the processed image
    processed_img = Image.fromarray(result.astype(np.uint8))
    processed_img.save('processed_image.jpg')
    print("Processed image saved as 'processed_image.jpg'")


# Divide the image among processes
local_start = rank * local_shape
local_end = (rank + 1) * local_shape
local_image = image[local_start:local_end]

# Define convolution kernels
kernel_sizes = {'red': 11, 'green': 7, 'blue': 3}
colors = ('red', 'green', 'blue')

if rank < len(colors):  # Processes for predefined colors
    color = colors[rank]
    kernel_size = kernel_sizes[color]
else:  # Extra processes use random colors and kernels
    color = f"random_{rank}"
    kernel_size = np.random.randint(3, 12)

# Apply convolution if a color is assigned
if color is not None:
    kernel = np.ones((kernel_size, kernel_size)) / kernel_size**2
    local_result = np.zeros_like(local_image)

    for i in range(local_image.shape[2]):  # Iterate over RGB channels
        local_result[:, :, i] = convolve(local_image[:, :, i], kernel)
else:
    local_result = np.zeros_like(local_image)

# Gather results
result = None
if rank == 0:
    result = np.zeros_like(image)

comm.Gather(local_result, result, root=0)

# Save the original and processed images on the root process
if rank == 0:
    # Save the original image
    original_img = Image.fromarray(image.astype(np.uint8))
    original_img.save('original_image.jpg')
    print("Original image saved as 'original_image.jpg'")

    # Save the processed image
    processed_img = Image.fromarray(result.astype(np.uint8))
    processed_img.save('processed_image.jpg')
    print("Processed image saved as 'processed_image.jpg'")
