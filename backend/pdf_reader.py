#this function will read the pdf files and use OCRmyPDF to add text to scanned pages. 
import os
import PyPDF2
from gpt_analysis import find_splits, PageSplits
from pdf_splitter import split_pdf_at_pages
import json

#this function takes a file path and opens the pdf, and extracts the text from the first page.
def pdf_OCR(file_path) -> str:
    test_file = file_path

    os.system(f'docker tag jbarlow83/ocrmypdf-alpine ocrmypdf')
    os.system(f'docker run -i --rm jbarlow83/ocrmypdf - -  <{test_file} >output.pdf')

    complete_file_text = ""
        
    with open('output.pdf', 'rb') as pdf:
        reader = PyPDF2.PdfReader(pdf)
        for page_num in range(len(reader.pages)): # reader.pages:
            text = reader.pages[page_num].extract_text()
            page_number = page_num
            complete_file_text += "Start Page: " + str(page_number) + "\n" + text + "\n" + "End Page: " + str(page_number) + "\n"
    return complete_file_text

test_file = "C:\\Users\\joelp\\mail-sort\\backend\\testdocument.pdf"
text = pdf_OCR(test_file)
gpt_response = find_splits(text) 
#gpt_response = PageSplits(new_pages=[5, 9, 14])
split_pdf_at_pages(gpt_response, test_file)
