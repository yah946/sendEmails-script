# Email Sending Script – Stage / Job Application

## Description

Cet outil permet d'envoyer automatiquement des candidatures (CV et lettre de motivation) à plusieurs entreprises en personnalisant les emails selon le genre et le nom du RH. Il est conçu pour un usage sûr, en respectant les limites d'envoi pour éviter le spam, et pour les utilisateurs qui souhaitent envoyer des candidatures rapidement et efficacement.

---

## Prérequis

- **Python 3** installé sur votre ordinateur (3.8 ou supérieur recommandé)  
- Connexion Internet active  
- Création d'un **mot de passe d'application** pour votre compte Gmail :  
    1. Connectez-vous à votre compte Google.  
    2. Allez dans `Compte Google > Sécurité > Mots de passe des applications`.  
    3. Créez un mot de passe pour **Mail** et **Windows / Mac**.  
    4. Copiez ce mot de passe pour le mettre dans le fichier `.env`.
---

## Installation

```
git clone https://github.com/yah946/sendEmails-script.git
pip install -r requirements.txt
python main.py

```
---

## Configuration

1. **Fichier `.env`** :  
   - Créez un fichier `.env` à partir du fichier exemple `.env.example`.  
   - Remplissez les variables suivantes :
        ```env
        EMAIL_ADDRESS=your_email@gmail.com
        EMAIL_PASSWORD=16CharAppPassword
        CV_FILE=CV_Prenom_Nom.pdf
        LETTER_MOTIVATION_FILE=Letter_Motivation_Prenom_Nom.pdf
        ```

2. **Pièces jointes** (dossier `Attachment`) :  
   - Placez votre CV (`CV_Prenom_Nom.pdf`) et votre lettre de motivation (`Letter_Motivation_Prenom_Nom.pdf`) dans le dossier `Attachment`.

3. **Modèle d'email** (`email_template.py` dans `Attachment`) :  
   - Définissez l'objet de l'email :  

        ```python
        MESSAGE_SUBJECT = "Demande de stage en développement web"
        ```
### Définition du corps du message

Définissez le corps du message dans la fonction `message(salutation)` en utilisant :
- la variable `INDENT` pour l'indentation de chaque paragraphe  
- la variable `salutation` pour l'introduction

```python
def message(salutation):
    # 4 espaces au début de chaque paragraphe
    INDENT = "    "
    # le message
    return f"""
{salutation},

{INDENT}Je me permets de vous...

{INDENT}Actuellement en formation dans le domaine du développement web...

{INDENT}Motivé, sérieux et désireux d'apprendre...
"""
```
## Fichier `emails.csv`

Contient les adresses e-mails des destinataires ainsi que leurs informations permettant de personnaliser l'e-mail.

### Colonnes

| Colonne | Description |
|-------|------------|
| `email` | Adresse e-mail du destinataire |
| `gender` | `0` = neutre, `1` = homme, `2` = femme |
| `rh_name` | Nom du RH si exist |

### Exemple de `emails.csv` (comma-separated value)

```csv
email,companyName,gender,rh,rh_name
othman@gmail.com,,1,1,Othman
companyX@gmail.com,ComanyX,0,0,
companyY@gmail.com,ComanyY,0,0,
khadija@gmail.com,ComanyZ,2,1,Khadija
```
## Limitations d'envoi

- **Comptes Gmail existants** : jusqu'à **25 exécutions / jour**, avec un maximum de **500 e-mails**.
- **Nouveaux comptes Gmail** : jusqu'à **150 e-mails / jour**.
- Le script envoie **1 e-mail par destinataire**, sans **Cc** ni **Bcc**.
- Une **connexion Internet** est requise pour l'envoi.

## Utilisation

1. Placez vos fichiers dans le dossier `Attachment`.
2. Remplissez le fichier `.env` avec :
   - votre adresse e-mail,
   - votre mot de passe d'application,
   - votre CV,
   - votre lettre de motivation.
3. Vérifiez le fichier `emails.csv` (**maximum 20 destinataires par exécution**).

4. Exécutez le script :

```bash
python main.py

```

