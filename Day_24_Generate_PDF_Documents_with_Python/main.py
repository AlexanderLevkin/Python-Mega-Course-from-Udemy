from fpdf import FPDF
import pandas as pd

df = pd.read_csv('topics.csv', sep=',')
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)


for index, row in df.iterrows():
    pdf.add_page()
    # header text
    pdf.set_font('Helvetica', size=20, style='B')
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=f'{row["Topic"]}', align='L', ln=1)
    pdf.line(10, 20, 200, 20)


    pdf.ln(265)
    pdf.set_font('Helvetica', size=10, style='B')
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=f'{row["Topic"]}', align='R', ln=1)

    for i in range(20, 298, 10):
        pdf.line(10, i, 200, i)

    for i in range(row['Pages'] - 1):
        # footer text
        pdf.ln(277)
        pdf.set_font('Helvetica', size=10, style='B')
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=12, txt=f'{row["Topic"]}', align='R', ln=1)


pdf.output('output.pdf')
