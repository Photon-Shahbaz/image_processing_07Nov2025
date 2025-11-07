from PIL import Image, ImageDraw

image_path = "images/input/GD.png"
output_path = "images/static/GD000.png"
coordinates_list = [(519, 389, 575, 402), (760, 341, 952, 565), (40, 743, 662, 770), (719, 649, 828, 761), (843, 650, 940, 764), (40, 924, 662, 950),
                    (720, 832, 834, 944), (843, 828, 946, 949), (303, 959, 368, 973), (303, 1000, 381, 1017), (301, 979, 359, 994), (748, 1002, 836, 1016), (39, 1118, 102, 1133), (280, 1082, 360, 1287)]

def hide_portion(image_path, output_path, coordinates_list):

    # Open the image
    img = Image.open(image_path)

    # Create a mask with the specified coordinates
    mask = Image.new('L', img.size, 255)
    draw = ImageDraw.Draw(mask)

    # draws a rectangle for each set of coordinates
    for coordinates in coordinates_list:
        draw.rectangle(coordinates, fill=0)


    # Invert the mask (to hide the specified portion)
    mask = Image.eval(mask, lambda x: 255 - x)

    # Apply the mask to the image
    img.paste((255, 255, 255), mask)

    # Save the result
    img.save(output_path)

# Example usage:
# image_path = 'images/example.png'
# output_path = 'images/example_hidden.png'
# coordinates = (100, 100, 200, 200)  # Specify the coordinates (left, top, right, bottom)

hide_portion(image_path, output_path, coordinates_list)
