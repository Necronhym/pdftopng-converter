#pip install PyMuPDF

import fitz  # PyMuPDF
from pathlib import Path

def convert_pdfs_to_pngs():
    pdf_files = list(Path('.').glob('*.pdf'))

    for pdf_file in pdf_files:
        pdf_document = fitz.open(pdf_file)

        for page_number in range(pdf_document.page_count):
            page = pdf_document[page_number]         
            image_bytes = page.get_pixmap().tobytes()

            png_filename = f"{pdf_file.stem}_page_{page_number + 1}.png"
            with open(png_filename, 'wb') as png_file:
                png_file.write(image_bytes)

        pdf_document.close()

if __name__ == "__main__":
    convert_pdfs_to_pngs()