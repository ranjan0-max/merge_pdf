import PyPDF2
import os

name = input("Enter the name of the PDF: ")
merger = PyPDF2.PdfMerger()  # Use PdfMerger instead of PdfFileMerger

for i in os.listdir():
    if i.endswith(".pdf"):
        try:
            merger.append(i)
            print(f"Added: {i}")
        except PyPDF2.errors.PdfReadError:
            print(f"Error reading {i}. It may be corrupted or invalid.")

merger.write(f"{name}.pdf")
merger.close()  # Close the merger
