import os
import sys
from pypdf import PdfWriter


def get_folder_path() -> str:
    while True:
        folder_path = input("Folder path of PDFs to merge: ").strip()
        if os.path.isdir(folder_path):
            return folder_path
        print("Provide a valid folder path.")


def get_output_filename() -> str:
    while True:
        output_filename = input("Filename for the output PDF: ").strip()
        if not output_filename:
            print("Filename cannot be empty.")
            continue
        if not output_filename.lower().endswith(".pdf"):
            output_filename += ".pdf"
        return output_filename


def find_pdf_files(folder_path: str) -> list:
    pdfs = [f for f in os.listdir(folder_path) if f.lower().endswith(".pdf")]
    pdfs.sort()
    return pdfs


def merge_pdfs(pdf_files: list, folder_path: str, output_filename: str):
    output_path = os.path.join(folder_path, output_filename)

    merger = PdfWriter()

    if output_filename in pdf_files:
        print("Skipped output file(s) with name matching one of the input PDFs.")
        pdf_files = [f for f in pdf_files if f != output_filename]

    if not pdf_files:
        print("No PDF files located.")
        sys.exit(1)

    for pdf in pdf_files:
        try:
            full_path = os.path.join(folder_path, pdf)
            merger.append(full_path)
        except Exception as e:
            print(f"Failed to add '{pdf}': {e}")

    try:
        merger.write(output_path)
        merger.close()
        print(f"Saved merged PDF as '{output_filename}' in '{folder_path}'")
    except Exception as e:
        print(f"Failed to write merged PDF: {e}")
        sys.exit(1)


def pdf_merger():
    folder_path = get_folder_path()
    output_filename = get_output_filename()
    pdf_files = find_pdf_files(folder_path)
    merge_pdfs(pdf_files, folder_path, output_filename)


if __name__ == "__main__":
    pdf_merger()
