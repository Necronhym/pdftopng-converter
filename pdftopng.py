# pip install PyMuPDF

import fitz  # PyMuPDF
from pathlib import Path

def sanitize_filename(filename):
    return filename.replace("  ", " ")

def convert_pdfs_to_pngs():
    print("Searching for PDF files...")
    pdf_files = list(Path('.').glob('*.pdf'))
    if not pdf_files:
        print("No PDF files found.")
        return

    for pdf_file in pdf_files:
        print(f"Processing: {pdf_file}")
        pdf_document = fitz.open(pdf_file)

        for page_number in range(pdf_document.page_count):
            page = pdf_document[page_number]
            pixmap = page.get_pixmap()
            image_bytes = pixmap.tobytes("png")

            # Generate sanitized PNG filename
            png_filename = sanitize_filename(f"{pdf_file.stem}_page_{page_number + 1}.png")
            print(f"Saving: {png_filename}")

            with open(png_filename, 'wb') as png_file:
                png_file.write(image_bytes)

        pdf_document.close()

if __name__ == "__main__":
    convert_pdfs_to_pngs()
