from PIL import Image, ImageDraw, ImageFont
import os
from datetime import datetime
from reportlab.pdfgen import canvas


importer = "ELITE CHEMICALS COMPANY"
invoice_value = "AED 990.30"
supplier_name = "SOAPS & CHEMICALS INDUSTRIAL & TRADING"
hs_code = "3204.1400"
port_of_loading = "ANY UAE AIRPORT"
ETA = "30.12.2025"
material_description = "DIRECT BLUE 86"
origin = "UK"
pfi_num = " # SC-03/11/25"
pfi_date = "03-11-2025"
inv_value_in_words = "abc"
unit_n_quantity = "00"
incoterm = "FCA"
address = "00"
def undertaking_eight_points(image_path, output_path, text_coordinates):
    # Open the image
    img = Image.open(image_path).convert('RGBA')

    # Create a drawing object
    draw = ImageDraw.Draw(img)

    # Define a font size and color
    font_size = 16
    font_color = (0, 0, 0, 255)  # Black in RGBA format

    # Use a TrueType font with the specified size
    font = ImageFont.truetype("arial.ttf", font_size)

    # Write text at specified coordinates
    for text, coordinates in text_coordinates:
        draw.text(coordinates, text, font=font, fill=font_color)

    # Save the result
    img.save(output_path, format='PNG')

# Example usage:
image_path = 'images/input/undertaking_8points.png'
output_path = 'images/static/8points.png'


# Get today's date in the format YYYY-MM-DD
today_date = datetime.now().strftime('%d-%m-%Y')

# List of tuples containing text and coordinates
text_coordinates = [
    (today_date, (843, 210)),
    (invoice_value, (801, 368)),
    (supplier_name, (116, 399)),
    (hs_code, (546, 479))
    # Add more text and coordinates as needed
]

undertaking_eight_points(image_path, output_path, text_coordinates)

##############################################################################

def form_v_31(image_path, output_path, text_coordinates):
    # Open the image
    img = Image.open(image_path).convert('RGBA')

    # Create a drawing object
    draw = ImageDraw.Draw(img)

    # Define a font size and color
    font_size = 16
    font_color = (0, 0, 0, 255)  # Black in RGBA format

    # Use a TrueType font with the specified size
    font = ImageFont.truetype("arial.ttf", font_size)

    # Write text at specified coordinates
    for text, coordinates in text_coordinates:
        draw.text(coordinates, text, font=font, fill=font_color)

    # Save the result
    img.save(output_path, format='PNG')

# Example usage:
image_path = 'images/input/V-31.png'
output_path = 'images/static/V-31.png'


# Get today's date in the format YYYY-MM-DD
today_date = datetime.now().strftime('%d-%m-%Y')

# List of tuples containing text and coordinates
text_coordinates = [
    (today_date, (191, 1577)),
    (invoice_value, (357, 433)),
    (supplier_name, (644, 435)),
    (port_of_loading, (138, 512)),
    (ETA, (664, 544)),
    (supplier_name, (174, 1142)),
    (invoice_value, (371, 1174)),
    (material_description, (563, 1142)),
    (origin, (870, 1168)),
    (importer, (519, 405)),
    (importer, (298, 1271)),
    (hs_code, (565, 1170))
    # Add more text and coordinates as needed
]

form_v_31(image_path, output_path, text_coordinates)

#############################################################################3

def stamp_paper(image_path, output_path, text_coordinates):
    # Open the image
    img = Image.open(image_path).convert('RGBA')

    # Create a drawing object
    draw = ImageDraw.Draw(img)

    # Define a font size and color
    font_size = 16
    font_color = (0, 0, 0, 255)  # Black in RGBA format

    # Use a TrueType font with the specified size
    font = ImageFont.truetype("arial.ttf", font_size)

    # Write text at specified coordinates
    for text, coordinates in text_coordinates:
        draw.text(coordinates, text, font=font, fill=font_color)

    # Save the result
    img.save(output_path, format='PNG')

# Example usage:
image_path = 'images/input/stamp_paper.png'
output_path = 'images/static/stamp_paper.png'


# Get today's date in the format YYYY-MM-DD
today_date = datetime.now().strftime('%d-%m-%Y')

# List of tuples containing text and coordinates
text_coordinates = [
    (today_date, (869, 628)),
    (supplier_name, (777, 953)),
    (invoice_value, (775, 1021)),
    (material_description, (776, 981)),
    (pfi_num, (778, 866)),
    (pfi_date, (775, 923)),
    (importer, (152, 1100))
    # Add more text and coordinates as needed
]

stamp_paper(image_path, output_path, text_coordinates)

#####################################################################

def related_party(image_path, output_path, text_coordinates):
    # Open the image
    img = Image.open(image_path).convert('RGBA')

    # Create a drawing object
    draw = ImageDraw.Draw(img)

    # Define a font size and color
    font_size = 16
    font_color = (0, 0, 0, 255)  # Black in RGBA format

    # Use a TrueType font with the specified size
    font = ImageFont.truetype("arial.ttf", font_size)

    # Write text at specified coordinates
    for text, coordinates in text_coordinates:
        draw.text(coordinates, text, font=font, fill=font_color)

    # Save the result
    img.save(output_path, format='PNG')

# Example usage:
image_path = 'images/input/related party indemnity.png'
output_path = 'images/static/related party indemnity.png'


# Get today's date in the format YYYY-MM-DD
today_date = datetime.now().strftime('%d-%m-%Y')

# List of tuples containing text and coordinates
text_coordinates = [
    (today_date, (899, 166)),
    (invoice_value, (899, 200)),
    (supplier_name, (399, 232)),
    (pfi_num, (899, 240)),
    (importer, (237, 280)),
    (importer, (242, 526)),
    (importer, (234, 982)),

    # Add more text and coordinates as needed
]

related_party(image_path, output_path, text_coordinates)

##############################################################

def convert_all_to_pdf(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Process each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".png"):  # Adjust the file extension as needed
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename.replace('.png', '.pdf'))

            convert_to_pdf(input_path, output_path)

def convert_to_pdf(image_path, pdf_path):
    # Load the image
    img = Image.open(image_path)

    # Get the image size
    width, height = img.size

    # Create a PDF canvas
    c = canvas.Canvas(pdf_path, pagesize=(width, height))

    # Draw the image on the PDF canvas
    c.drawInlineImage(image_path, 0, 0, width, height)

    # Save the PDF
    c.save()

# Example usage:
input_folder = 'images/static/'
output_folder = 'images/static/'

convert_all_to_pdf(input_folder, output_folder)