#!/usr/bin/env python3
"""Lily House form handler — POST → email via SMTP. Zero deps, stdlib only."""
import os, ssl, smtplib, urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
from email.mime.text import MIMEText

SMTP_HOST = os.environ["SMTP_HOST"]
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.environ["SMTP_USER"]
SMTP_PASS = os.environ["SMTP_PASS"]
TO_EMAIL = os.environ["TO_EMAIL"]

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(length).decode()
        params = dict(urllib.parse.parse_qsl(raw))

        lines = [f"Form: {self.path}", ""]
        for k, v in params.items():
            k = k.replace("_", " ").title()
            lines.append(f"{k}: {v}")
        body = "\n".join(lines)

        msg = MIMEText(body)
        msg["From"] = SMTP_USER
        msg["To"] = TO_EMAIL
        msg["Subject"] = f"Lily House — {self.path.strip('/').title()}"

        ctx = ssl.create_default_context()
        s = smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=10)
        s.starttls(context=ctx)
        s.login(SMTP_USER, SMTP_PASS)
        s.send_message(msg)
        s.quit()

        self.send_response(302)
        self.send_header("Location", "/?sent=1")
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"ok")

if __name__ == "__main__":
    port = int(os.getenv("PORT", "8080"))
    HTTPServer(("0.0.0.0", port), Handler).serve_forever()
