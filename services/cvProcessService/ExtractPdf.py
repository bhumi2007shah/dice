import PyPDF2
import textract
import io
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

def extract_from_pdf(file, file_path):
    text = ""
    '''
    if file_path is not None:
        text = textract.process(file_path, method='tesseract', language='eng')
	'''
    if text != "":
        return text
    '''
    else:
        pdfReader = PyPDF2.PdfFileReader(file)
        pagesCount = pdfReader.numPages
        for i in range(0, pagesCount):
            pageObj = pdfReader.getPage(i)
            text += pageObj.extractText()
    '''
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
    
    with open(file_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh, 
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)
            
        text = fake_file_handle.getvalue()
    
    # close open handles
    converter.close()
    fake_file_handle.close()
    
    if text:
        return text
    
    return text


# calling above function and extracting text
def extract_text_from_pdf(file_path):
    text = extract_from_pdf(file_path)
    if text != "":
        return text
    else:
        print("nothing extrated from pdf file")
