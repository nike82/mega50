from fpdf import FPDF
import glob
from pathlib import Path

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
file_paths = glob.glob("invoices/*.txt")

pdf = FPDF(orientation="P", unit="mm", format="A4")

for file_path in file_paths:
    pdf.add_page()
    page_name = Path(file_path).stem.title()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=page_name, ln=1)

    with open(file_path) as file:
        content = file.read()

    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(w=0, h=6, txt=content)

pdf.output("PDFs/output.pdf")
