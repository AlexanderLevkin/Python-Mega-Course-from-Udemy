import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()

    filename = Path(filepath).stem
    invoice_name, date = filename.split('-')

    pdf.set_font('Arial', size=16, style='B')
    pdf.cell(w=50, h=8, txt=f'Invoice nr. {invoice_name}', ln=1)

    pdf.set_font('Arial', size=16, style='B')
    pdf.cell(w=50, h=8, txt=f'Date: {date}', ln=1)

    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    header = df.columns
    header = [item.replace('_', ' ').title() for item in header]

    pdf.set_font('Helvetica', size=10, style='B')
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=str(header[0]), border=1, align='C')
    pdf.cell(w=70, h=8, txt=str(header[1]), border=1, align='C')
    pdf.cell(w=40, h=8, txt=str(header[2]), border=1, align='C')
    pdf.cell(w=30, h=8, txt=str(header[3]), border=1, align='C')
    pdf.cell(w=30, h=8, txt=str(header[4]), border=1, align='C', ln=1)

    for index, row in df.iterrows():
        pdf.set_font('Arial', size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1, align='C')
        pdf.cell(w=70, h=8, txt=str(row["product_name"]), border=1, align='C')
        pdf.cell(w=40, h=8, txt=str(row["amount_purchased"]), border=1, align='C')
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1, align='C')
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, align='C', ln=1)

    total_sum = df["total_price"].sum()

    pdf.set_font('Arial', size=10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, border=1, align='C')
    pdf.cell(w=70, h=8, border=1, align='C')
    pdf.cell(w=40, h=8, border=1, align='C')
    pdf.cell(w=30, h=8, border=1, align='C')
    pdf.cell(w=30, h=8, txt=str(total_sum), border=1, align='C', ln=1)
    pdf.cell(w=30, h=8, ln=1)

    pdf.set_font('Arial', size=16, style='B')
    pdf.cell(w=50, h=8, txt="Total Sum:" + str(total_sum), ln=1)

    pdf.cell(w=35, h=8, txt="PythonHow")
    pdf.image('pythonhow.png', w=10)

    pdf.output(f'pdfs/{invoice_name}.pdf')

