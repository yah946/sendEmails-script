from fpdf import FPDF
INDENT = "      "
#Your Information
FULL_NAME = 'Full Name'
PHONE_NUMBER = 'Phone Number'
EMAIL_ADDRESS = 'Email Address'
#Email Body
def letter(salutation,companyName):
#Recruiter Information
    MOTIVATION_LETTER = (f"""
        {salutation}
        
        {INDENT}Actuellement étudiant...

        {INDENT}Au cours de ma formation...

        {INDENT}Motivé, sérieux...

        {INDENT}Je serais honoré ...

        {INDENT}Dans l'attente de votre retour, je vous prie d'agréer, {salutation} l'expression de mes salutations distinguées.
    """)
    return MOTIVATION_LETTER

def string2pdf(content,output_filename='Attachment\Lettre_Motivation_Premon_Nom.pdf'):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Times','',12)

    pdf.cell(0, 8, FULL_NAME,ln=True)
    pdf.cell(0, 8, PHONE_NUMBER,ln=True)
    pdf.cell(0, 8, EMAIL_ADDRESS,ln=True)

    pdf.cell(0, 8, "À l'attention du recruteur", ln=True, align='R')
    # pdf.cell(0, 8, "Casablanca", ln=True, align='R')

    for paragraph in content.split('\n'):
        pdf.multi_cell(0, 8, f"{paragraph}")
    
    pdf.cell(0, 8, FULL_NAME,ln=True)

    pdf.output(output_filename)