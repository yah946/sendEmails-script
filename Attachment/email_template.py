import textwrap as wrap
INDENT = "\t"
#Subject Here
MESSAGE_SUBJECT = "Subject Here..."
#Email Body
def message(salutation,companyName):
    MESSAGE_BODY = wrap.dedent(f"""\
        {salutation}

        {INDENT}Je me permets de vous contacter afin de vous soumettre ma candidature pour un stage en développement web au sein {companyName}.

        {INDENT}Actuellement en formation ...

        {INDENT}Motivé, sérieux ...

        {INDENT}Vous trouverez ci-joint ...

        {INDENT}Je reste à votre entière ...

        {INDENT}Je vous prie d'agréer, {salutation} l'expression de mes salutations distinguées.

        Full Name
        Domain Name
        Phone Number
        Email
        LinkedIn: url
        GitHub: https://github.com/<username>
    """)
    return MESSAGE_BODY