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


def find_latest_pdf():
    """Return the most recently generated executive summary PDF."""
    pdfs = sorted(REPO_DIR.glob("PetFactory_Maroc_Resume_Executif_*.pdf"), reverse=True)
    if not pdfs:
        sys.exit("ERROR: No executive summary PDF found in repo root.")
    return pdfs[0]


def load_service_account():
    """Load service account credentials from env var or fallback file."""
    raw = os.environ.get("PETFACTORY_SERVICE_ACCOUNT_JSON")
    if raw:
        return json.loads(raw)
    fallback = Path.home() / ".petfactory" / "service_account.json"
    if fallback.exists():
        return json.loads(fallback.read_text())
    sys.exit(
        "ERROR: No service account credentials found.\n"
        "Set PETFACTORY_SERVICE_ACCOUNT_JSON env var or place the key at "
        "~/.petfactory/service_account.json"
    )


def build_gmail_service(sa_info):
    from google.oauth2 import service_account
    from googleapiclient.discovery import build

    creds = service_account.Credentials.from_service_account_info(
        sa_info, scopes=SCOPES
    ).with_subject(SENDER)  # impersonate sender via domain-wide delegation

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

    sa_info = load_service_account()
    service = build_gmail_service(sa_info)

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
