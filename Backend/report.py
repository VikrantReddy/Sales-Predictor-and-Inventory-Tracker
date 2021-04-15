from fpdf import FPDF
  
def generate_report(): 
    pdf = FPDF()

    pdf.add_page()
  
    pdf.set_font("Arial", size = 15)

    pdf.cell(200, 10, txt = "Sales report March", 
         ln = 1, align = 'C')

    pdf.cell(200,10, txt="Weekly Revenue",ln=2,align="L")
    pdf.cell(200,10, txt="Monthly Revenue",ln=3,align="L")

    pdf.cell(200,10, txt="$8740",ln=3,align="L")
    pdf.cell(200,10, txt="$40000",ln=4,align="L")

    pdf.output("reports/report1.pdf")   

if __name__ == "__main__":
    generate_report()