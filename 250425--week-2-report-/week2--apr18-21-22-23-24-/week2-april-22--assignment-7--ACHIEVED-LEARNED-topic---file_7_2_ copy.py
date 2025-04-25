########################################################

########################################################
# learned lessons and topic covered . # solution --- ACHIEVED-LEARNED_topic
########################################################
########################################################
import csv
from fpdf import FPDF

# File paths
csv_file = "file7.csv"
pdf_file = "file7_2.pdf"

# Initialize the PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Title of the PDF
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, txt="Recipe Book", ln=1, align='C')
pdf.ln(10)  # Line break

# Load CSV and write to PDF
with open(csv_file, "r") as file:
    reader = csv.reader(file)
    headers = next(reader)  # Skip the header
    
    pdf.set_font("Arial", 'B', 12)
    for header in headers:
        pdf.cell(50, 10, txt=header, border=1)
    pdf.ln()
    
    pdf.set_font("Arial", size=12)
    for row in reader:
        # Ensure all fields are properly handled
        title = row[0]
        ingredients = row[1]
        steps = row[2]
        tags = row[3]

        pdf.cell(50, 10, txt=title[:30], border=1)
        pdf.cell(50, 10, txt=ingredients[:30], border=1)
        pdf.cell(50, 10, txt=steps[:30], border=1)
        pdf.cell(50, 10, txt=tags[:30], border=1)
        pdf.ln()

# Save PDF
pdf.output(pdf_file)
print(f"PDF exported successfully to '{pdf_file}'")
