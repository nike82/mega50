import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

file_paths = glob.glob("invoices/*.xlsx")

for file_path in file_paths:
    df = pd.read_excel(file_path, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    file_name = Path(file_path).stem
    invoice_nr = file_name.split("-")[0]
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_nr}")
    pdf.output(f"PDFs/{file_name}.pdf")
