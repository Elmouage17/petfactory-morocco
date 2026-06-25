#!/usr/bin/env python3
"""
Send the latest PetFactory Maroc weekly PDF report via Gmail API.

Requires:
  - google-auth, google-auth-httplib2, google-api-python-client
  - PETFACTORY_SERVICE_ACCOUNT_JSON env var (contents of the service account key file)
  - OR a file at ~/.petfactory/service_account.json

Service account must have domain-wide delegation with scope:
  https://www.googleapis.com/auth/gmail.send
"""

import os, sys, json, glob, base64, mimetypes
from email.message import EmailMessage
from pathlib import Path

# ── config ────────────────────────────────────────────────────────────────────
SENDER      = "s.elaribi@petfactory.ma"
RECIPIENTS  = ["h.rahali@petfactory.ma"]
SUBJECT     = "PetFactory Maroc — Résumé Exécutif Hebdomadaire"
BODY_TEXT   = """\
Bonjour,

Veuillez trouver ci-joint le résumé exécutif hebdomadaire du projet PetFactory Maroc.

Ce rapport couvre :
  • Statut RAG des 7 systèmes principaux
  • Risques principaux et actions prioritaires
  • Échéancier des jalons à 5 mois

Cordialement,
Sam Aribi — Chef de Projet
PetFactory Maroc
"""
SCOPES      = ["https://www.googleapis.com/auth/gmail.send"]
REPO_DIR    = Path(__file__).resolve().parent.parent

# OAuth credentials — loaded from environment variables (never hardcoded)
# Set these in your shell profile or CI environment:
#   export PETFACTORY_GMAIL_CLIENT_ID="..."
#   export PETFACTORY_GMAIL_CLIENT_SECRET="..."
#   export PETFACTORY_GMAIL_REFRESH_TOKEN="..."
CREDS_FILE  = Path.home() / ".petfactory" / "gmail_oauth.json"


def find_latest_pdf():
    """Return the most recently generated executive summary PDF."""
    pdfs = sorted(REPO_DIR.glob("PetFactory_Maroc_Resume_Executif_*.pdf"), reverse=True)
    if not pdfs:
        sys.exit("ERROR: No executive summary PDF found in repo root.")
    return pdfs[0]


def load_oauth_creds():
    """Load OAuth credentials from env vars or fallback file."""
    client_id     = os.environ.get("PETFACTORY_GMAIL_CLIENT_ID")
    client_secret = os.environ.get("PETFACTORY_GMAIL_CLIENT_SECRET")
    refresh_token = os.environ.get("PETFACTORY_GMAIL_REFRESH_TOKEN")

    if not all([client_id, client_secret, refresh_token]):
        if CREDS_FILE.exists():
            data = json.loads(CREDS_FILE.read_text())
            client_id     = data.get("client_id")
            client_secret = data.get("client_secret")
            refresh_token = data.get("refresh_token")

    if not all([client_id, client_secret, refresh_token]):
        sys.exit(
            "ERROR: Gmail OAuth credentials not found.\n"
            "Set env vars PETFACTORY_GMAIL_CLIENT_ID, PETFACTORY_GMAIL_CLIENT_SECRET, "
            "PETFACTORY_GMAIL_REFRESH_TOKEN\n"
            f"or place credentials at {CREDS_FILE}"
        )
    return client_id, client_secret, refresh_token


def build_gmail_service():
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build

    client_id, client_secret, refresh_token = load_oauth_creds()
    creds = Credentials(
        token=None,
        refresh_token=refresh_token,
        token_uri="https://oauth2.googleapis.com/token",
        client_id=client_id,
        client_secret=client_secret,
        scopes=SCOPES,
    )
    return build("gmail", "v1", credentials=creds, cache_discovery=False)


def build_message(pdf_path: Path) -> str:
    msg = EmailMessage()
    msg["From"]    = SENDER
    msg["To"]      = ", ".join(RECIPIENTS)
    msg["Subject"] = SUBJECT
    msg.set_content(BODY_TEXT)

    mime_type, _ = mimetypes.guess_type(str(pdf_path))
    main, sub = (mime_type or "application/octet-stream").split("/", 1)
    msg.add_attachment(
        pdf_path.read_bytes(),
        maintype=main,
        subtype=sub,
        filename=pdf_path.name,
    )
    return base64.urlsafe_b64encode(msg.as_bytes()).decode()


def main():
    pdf = find_latest_pdf()
    print(f"Attaching: {pdf.name}")

    service = build_gmail_service()

    encoded = build_message(pdf)
    result  = service.users().messages().send(
        userId="me",
        body={"raw": encoded}
    ).execute()

    print(f"Email sent — Message ID: {result['id']}")
    print(f"  From : {SENDER}")
    print(f"  To   : {', '.join(RECIPIENTS)}")
    print(f"  File : {pdf.name}")


if __name__ == "__main__":
    main()
