from docx import Document

def save_to_docx(text: str, filename: str = "Gereksinim_Dokumani.docx") -> None:
    doc = Document()
    for line in text.splitlines():
        doc.add_paragraph(line if line else "")
    doc.save(filename)
    print(f"✅  '{filename}' kaydedildi.")
