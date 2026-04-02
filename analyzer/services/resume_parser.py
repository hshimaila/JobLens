import pdfplumber
import docx
import os


class ResumeParser:
    def extract_text(self, file_path: str) -> str:
        if not os.path.exists(file_path):
            raise FileNotFoundError("Resume file not found")

        if file_path.endswith(".pdf"):
            return self._extract_pdf(file_path)

        elif file_path.endswith(".docx"):
            return self._extract_docx(file_path)

        else:
            raise ValueError("Unsupported file format")

    def _extract_pdf(self, file_path: str) -> str:
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text.strip()

    def _extract_docx(self, file_path: str) -> str:
        doc = docx.Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs]).strip()
