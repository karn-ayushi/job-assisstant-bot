from pypdf import PdfReader

def read_pdf(file):
    reader = PdfReader(file)
    pages_text = []

    for page in reader.pages:
        content = page.extract_text()
        if content:
            pages_text.append(content.strip())

    return "\n".join(pages_text)
