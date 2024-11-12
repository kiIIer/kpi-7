from PIL import Image
import numpy as np


def upscale_image_4x4(input_image_path, output_image_path):
    # Open the image
    img = Image.open(input_image_path)

    # Convert image to numpy array
    img_array = np.array(img)

    # Get the height, width, and channels of the image
    h, w, c = img_array.shape

    # Create an upscaled array by replicating each pixel into a 4x4 block
    upscaled_array = np.repeat(np.repeat(img_array, 8, axis=0), 8, axis=1)

    # Convert the numpy array back to an image
    upscaled_img = Image.fromarray(upscaled_array)

    # Save the upscaled image
    upscaled_img.save(output_image_path)


# Usage example
input_image_path = '/Users/killer/proj/KPI/kpi-7/data-sci/lab-1/view-dataset/image-3.png'  # Replace with your image path
upscale_image_4x4(input_image_path, input_image_path)
