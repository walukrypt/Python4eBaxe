import PyPDF2
import os

def extract_text_from_pdfs(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            with open(os.path.join(directory, filename), "rb") as file:
                reader = PyPDF2.PdfReader(file)
                text = ""
                for page in reader.pages:
                    text += page.extract_text()
                with open(f"{filename}.txt", "w", encoding="utf-8") as txt_file:
                    txt_file.write(text)

# Example: extract_text_from_pdfs("/path/to/pdfs")
