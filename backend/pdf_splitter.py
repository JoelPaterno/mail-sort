import PyPDF2
from gpt_analysis import PageSplits

def split_pdf_at_pages(page_numbers: PageSplits, pdf_file_path):
    # Open the PDF file
    with open(pdf_file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        total_pages = len(reader.pages)
        
        # Ensure the page numbers are sorted and unique
        #page_numbers = sorted(set(page_numbers))
        
        # Add the start and end pages to the list of split points
        page_numbers.new_pages.insert(0, 0)
        page_numbers.new_pages.append(total_pages)
        
        
        # Iterate through the split points and create new PDF files
        for i in range(len(page_numbers.new_pages) - 1):
            start_page = page_numbers.new_pages[i]
            end_page = page_numbers.new_pages[i + 1]
            
            # Create a new PDF writer for the split part
            writer = PyPDF2.PdfWriter()
            for page_num in range(start_page, end_page):
                writer.add_page(reader.pages[page_num])
                
            # Save the split part to a new file
            output_file_path = f'split_part_{i+1}.pdf'
            with open(output_file_path, 'wb') as output_file:
                writer.write(output_file)
            
            print(f'Saved: {output_file_path}')