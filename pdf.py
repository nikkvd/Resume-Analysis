from pypdf import PdfReader

def read_pdf(pdf_doc):
    pdf = PdfReader(pdf_doc)
    
    # Save the Information in raw text
    text = ''
    
    for i,page in enumerate(pdf.pages):
        content = page.extract_text()
        
        if content:
            text+=content
    return (text)