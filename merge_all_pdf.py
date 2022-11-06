import PyPDF2
import os

name=input("Enter the name of pdf :- ")
merger = PyPDF2.PdfFileMerger()
for i in os.listdir():
    if i.endswith(".pdf"):
        merger.append(i)
merger.write(f"{name}.pdf")
