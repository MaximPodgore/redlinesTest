from spire.doc import *
from spire.doc.common import *
from redlines import Redlines

def read_docx_to_string(file_path):
    # Create a Document object
    document = Document()
    
    # Load the .docx file
    document.LoadFromFile(file_path)
    
    # Extract the text of the document
    document_text = document.GetText()
    
    # Close the document (optional)
    document.Close()
    
    return document_text

init_text = read_docx_to_string("ASIMAKOPOLOUS CDA KARYOPHARM 53831 1_SOURCE.docx")
out_text = read_docx_to_string("output2.docx")
test = Redlines(init_text, out_text)
#could make a write function to port the output to a md file
print(test.output_markdown)