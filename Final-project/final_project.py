import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
subjek = "subjek"
isi = "isi email"
pengirim = "pengirim@gmail.com"
penerima = "penerima@gmail.com"
password = input("Type your password and press enter:")
message = MIMEMultipart()
message["From"] = pengirim
message["To"] = penerima
message["Subject"] = subjek
message.attach(MIMEText(isi, "plain"))
filename = "namafile.pdf" 
with open(filename, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)
message.attach(part)
text = message.as_string()
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(pengirim, password)
    server.sendmail(pengirim, penerima, text)