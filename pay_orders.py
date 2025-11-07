from PIL import Image, ImageDraw, ImageFont
import os
from datetime import datetime
from reportlab.pdfgen import canvas


GL = "ELITE CHEMICALS"
supplier_01 = "DSV AIR AND SEA PAKISTAN (SMC-PVT) LTD"
supplier_01_amount = "659,745"
supplier_02 = "HAPAG-LLOYD PAKISTAN PVT LTD"
supplier_02_amount = "92,400"
total_amount = "752,145"
total_amount_inwords= "Seven hundred fifty two thousand one hundred forty five only"
branch = 'New Challi'
account_no = "1 0 1 5 0 0 8 1 0 0 2 0 7 1 0 1 9"
cheque_no = ""
def pay_order_01(image_path, output_path, text_coordinates):
    # Open the image
    img = Image.open(image_path).convert('RGBA')

    # Create a drawing object
    draw = ImageDraw.Draw(img)

    # Define a font size and color
    font_size = 30
    font_color = (0, 0, 0, 255)  # Black in RGBA format

    # Use a TrueType font with the specified size
    font = ImageFont.truetype("arial.ttf", font_size)

    # Write text at specified coordinates
    for text, coordinates in text_coordinates:
        draw.text(coordinates, text, font=font, fill=font_color)

    # Save the result
    img.save(output_path, format='PNG')

# Example usage:
image_path = 'images/input/PayOrderForm01.png'
output_path = 'images/static/PayOrder01.png'


# Get today's date in the format YYYY-MM-DD
today_date = datetime.now().strftime('%d-%m-%Y')

# List of tuples containing text and coordinates
text_coordinates = [
    (today_date, (1311, 230)),
    (branch, (151, 250)),
    (account_no, (604, 340)),
    (cheque_no, (382, 395)),
    (supplier_01, (303, 595)),
    (supplier_01_amount, (1300, 645)),
    (supplier_02, (309, 873)),
    (supplier_02_amount, (1303, 922)),
    (total_amount, (294, 1160)),
    (total_amount_inwords, (665, 1160)),
    # Add more text and coordinates as needed
]

pay_order_01(image_path, output_path, text_coordinates)