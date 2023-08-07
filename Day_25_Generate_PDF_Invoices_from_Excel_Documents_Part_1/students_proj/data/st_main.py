import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("../data/*.txt")

pdf = FPDF(orientation='P', unit='mm', format='A4')

for filepath in filepaths:
    with open(filepath, 'r') as file:

        pdf.add_page()
        filename = Path(filepath).stem.capitalize()

        pdf.set_font('Arial', size=16, style='B')
        pdf.cell(w=50, h=8, txt=f'{filename.capitalize()}', ln=1, align='C')

pdf.output(f'../st_pdf/Output.pdf')
