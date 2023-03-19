import mimetypes
import os
import settings
import smtplib

from email import encoders
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(email_to, subject, body, fpath=None):
    msg = MIMEMultipart()
    msg['From'] = settings.EMAIL_FROM
    msg['To'] = email_to
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    print(f"\nMAILTO: {email_to} ")

    if fpath is not None:
        if os.path.isdir(fpath):
            # отправка содержимого папки
            attaches = _get_attaches(fpath)
            for attache in attaches:
                msg.attach(attache)
        elif os.path.isfile(fpath):
            # отправка файла
            attach = _get_attach_msg(fpath)
            if attach:
                msg.attach(attach)

    count = 0
    while True:
        count += 1
        try:
            server = smtplib.SMTP(settings.SMTP_SERVER, settings.SMTP_PORT)
            server.ehlo()
            server.starttls()
            server.login(settings.EMAIL_FROM, settings.EMAIL_PASS)
            text = msg.as_string()
            server.sendmail(settings.EMAIL_FROM, email_to, text)
            server.quit()
            break
        except BaseException:
            print(f"{count}. Can not send email: {email_to}")
            if count >= 5:
                print(f"ERROR: Sending mail skipped after: {count} attempts")
                break

    print("Ok\n")


def _get_attaches(path):
    _, _, attache_names = next(os.walk(path), (None, None, []))
    attaches = []
    for attache_name in attache_names:
        full_path = os.path.join(path, attache_name)
        attach = _get_attach_msg(full_path)
        if attach:
            attaches.append(attach)
    return attaches


def _get_attach_msg(path):
    """ make MIME type attachment message
    idea: https://gist.github.com/elprup/3205948
    """
    if not os.path.isfile(path):
        return
    c_type, encoding = mimetypes.guess_type(path)
    if c_type is None or encoding is not None:
        c_type = 'application/octet-stream'
    maintype, subtype = c_type.split('/', 1)

    print(path)
    with open(path, "rb") as fp:
        if maintype == 'text':
            _msg = MIMEText(fp.read(), _subtype=subtype)
        elif maintype == 'image':
            _msg = MIMEImage(fp.read(), _subtype=subtype)
        elif maintype == 'audio':
            _msg = MIMEAudio(fp.read(), _subtype=subtype)
        else:
            _msg = MIMEBase(maintype, subtype)
            _msg.set_payload(fp.read())
            encoders.encode_base64(_msg)

    filename = os.path.basename(path)
    _msg.add_header('Content-Disposition', 'attachment', filename=filename)
    return _msg
