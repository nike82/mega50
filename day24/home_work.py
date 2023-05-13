from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    # Set the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(r=100, g=100, b=100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)

    for y in range(20, 298, 10):
        pdf.line(x1=10, y1=y, x2=200, y2=y)

    # Set the footer
    pdf.ln(260)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.cell(w=0, h=20, txt=row["Topic"], align="R", ln=1)

    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # Set the footer
        pdf.ln(272)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.cell(w=0, h=20, txt=row["Topic"], align="R", ln=1)
        for y in range(20, 298, 10):
            pdf.line(x1=10, y1=y, x2=200, y2=y)

pdf.output("output_hw.pdf")

