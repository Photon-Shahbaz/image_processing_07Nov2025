import os
import fitz  # PyMuPDF
from PIL import Image


def convert_pdf_to_png(pdf_path, output_path, zoom=2):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    # Load the first (and only) page
    page = pdf_document.load_page(0)

    # Set zoom factor to increase resolution
    mat = fitz.Matrix(zoom, zoom)

    # Render the page to a Pixmap (image) with the specified zoom
    pix = page.get_pixmap(matrix=mat)

    # Convert Pixmap to an Image object
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

    # Save the image
    img.save(output_path)
    print(f"Saved {output_path}")


def convert_all_gd_pdfs():
    input_folder = r"C:\Users\HP\Downloads"
    output_folder = r"C:\Users\HP\PycharmProjects\Image_processing-master\images\input"

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files in the input folder
    for file_name in os.listdir(input_folder):
        # Check if the file starts with "GD" and has a .pdf extension
        if file_name.startswith("GD-") and file_name.endswith(".pdf"):
            pdf_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, file_name.replace(".pdf", ".png"))

            # Convert the PDF to PNG with improved quality
            convert_pdf_to_png(pdf_path, output_path, zoom=4)  # Increase zoom for higher resolution


# Run the conversion
convert_all_gd_pdfs()
