from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from datetime import datetime

def save_to_docx(text: str, filename: str = "Gereksinim_Dokumani.docx") -> None:
    doc = Document()

    # --- FORM BAŞLIĞI ve ÜST BİLGİLER ---
    heading = doc.add_heading("📄 Ürün Gereksinim Dokümanı", level=1)
    heading.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

    doc.add_paragraph()  # boşluk bırak

    table = doc.add_table(rows=5, cols=2)
    table.style = 'Table Grid'

    fields = [
        ("Form Adı", "Ürün Gereksinim Dokümanı"),
        ("Form Numarası", "FRM-PRD-001"),
        ("Versiyon", "1.0"),
        ("Hazırlayan", "Otomatik AI Sistem"),
        ("Tarih", datetime.today().strftime("%d.%m.%Y")),
    ]

    for i, (label, value) in enumerate(fields):
        table.cell(i, 0).text = label
        table.cell(i, 1).text = value

    doc.add_paragraph()  # boşluk bırak

    # --- GPT'den Gelen Metni Yaz ---
    for line in text.splitlines():
        clean_line = line.strip()
        if not clean_line:
            doc.add_paragraph()
        elif clean_line.startswith(tuple("1234567890")) and clean_line[1:3] == ". ":
            # Başlık formatı (örn: 1. Başlık)
            para = doc.add_paragraph()
            run = para.add_run(clean_line)
            run.bold = True
            run.font.size = Pt(12)
        elif clean_line.endswith(":"):
            para = doc.add_paragraph()
            run = para.add_run(clean_line)
            run.bold = True
            run.font.size = Pt(11)
        else:
            para = doc.add_paragraph(clean_line)
            para.paragraph_format.space_after = Pt(6)

    doc.save(filename)
    print(f"✅ '{filename}' başarıyla kaydedildi.")
