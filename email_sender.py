import smtplib
from email.message import EmailMessage
import mimetypes

def send_email(sender, password, receiver, subject, body, attachment=None):
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject
    msg.set_content(body)

    # 📎 Attachment handling (optional)
    if attachment is not None:
        file_name = attachment.name
        file_data = attachment.read()

        mime_type, _ = mimetypes.guess_type(file_name)
        if mime_type is None:
            mime_type = "application/octet-stream"

        maintype, subtype = mime_type.split("/", 1)

        msg.add_attachment(
            file_data,
            maintype=maintype,
            subtype=subtype,
            filename=file_name
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)
