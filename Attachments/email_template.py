import textwrap as wrap
INDENT = "      "

MESSAGE_SUBJECT = "Subject here..."

def message(salutation):
    MESSAGE_BODY = wrap.dedent(f"""\
        {salutation}

        {INDENT}Je me permets de vous contacter... (paragraph1)

        {INDENT}Actuellement en formation dans le domaine... (paragraph2)

        {INDENT}Motivé, sérieux et désireux d'apprendre... (paragraph3)

        {INDENT}Vous trouverez ci-joint... (paragraph4)

        {INDENT}Je reste à votre entière disposition... (paragraph5)

        {INDENT}Je vous prie d'agréer, {salutation} l'expression de mes salutations distinguées.

        Votre Nom
        Votre spécialité : Développement Web
        Votre numéro de téléphone
        Votre adresse e-mail
        LinkedIn: link here
        GitHub: link here
    """)
    return MESSAGE_BODY