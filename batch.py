import os
from PIL import Image, ImageDraw

def hide_portion(image_path, output_path, coordinates_list):
    # Open the image
    img = Image.open(image_path).convert("RGBA")

    # Create a mask with the specified coordinates for each portion
    mask = Image.new('L', img.size, 255)
    draw = ImageDraw.Draw(mask)

    for coordinates in coordinates_list:
        draw.rectangle(coordinates, fill=0)

    # Create an image with the same size and a white background
    white_image = Image.new('RGBA', img.size, (255, 255, 255, 255))

    # Apply the mask to the white image
    white_image.paste(img, mask=mask)

    # Save the result
    white_image.save(output_path)

def batch_process_images(input_folder, output_folder, coordinates_list):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Process each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".png"):  # Adjust the file extension as needed
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            hide_portion(input_path, output_path, coordinates_list)

# Example usage:
input_folder = 'images/input/'
output_folder = 'images/static/'
coordinates_list = [(1245, 929, 1391, 977), (1723, 1557, 2217, 1813), (95, 1769, 1529, 1845),
                    (95, 2217, 1507, 2280), (1723, 1990, 2177, 2251), (723, 2301, 867, 2441),
                    (1793, 2400, 1997, 2440), (670, 2593, 847, 3095), (95, 2675, 235, 2730),
                    (1827, 817, 2293, 1370)]
# Add more coordinates as needed

batch_process_images(input_folder, output_folder, coordinates_list)
