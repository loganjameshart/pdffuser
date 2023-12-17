"""
Merges all PDFs in the current working directory. 

The name for the new merged file should be provided as the first argument. Otherwise, the file's name will be the timestamp when it was created.
"""


import PyPDF2
import os
import sys
import datetime


NOW = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
CWD = os.getcwd()


def merge(file_list: list, new_filename=f"{NOW}-merged.pdf"):
    """Creates a merged PDF file from component PDF filepaths."""
    list_length = len(file_list)

    merged_pdf = PyPDF2.PdfFileMerger()
    for index, pdf_file in enumerate(file_list):
        merged_pdf.append(pdf_file)
        progress = int(((index + 1) / list_length) * 100) # gets percentage
        print(f"{progress}% of files merged.")

    merged_pdf.write(new_filename)
    merged_pdf.close()
    print("\nAll files merged.")


def get_pdfs():
    """Gets pathnames of PDF files in current working directory."""
    pdfs = []
    for filename in os.listdir(CWD):
        if filename.endswith(".pdf"):
            pdfs.append(os.path.realpath(filename))
    if not pdfs:
        print("No PDF files found in directory.")
        sys.exit(1)
    return pdfs


def main():
    pdf_list = get_pdfs()
    try:
        merged_filename = sys.argv[1]
        merge(pdf_list, new_filename=f"{merged_filename}.pdf")
    except IndexError:
        merge(pdf_list)


if __name__ == "__main__":
    main()
