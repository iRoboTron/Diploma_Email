"""
Postcardware License
Copyright (c) 2023 RoboTron
Email: iAdelfos@gmail.com
https://www.youtube.com/@RoboTron_Channel/
"""

import os

from src import email_sender

PATH = "out"
SUBJECT = "Документы нашего конкурса!"
BODY = """Здравствуйте!

Спасибо за участие в нашем конкурсе

--------------
С уважением команда RoboTron
"""

_, folders, _ = next(os.walk(PATH), (None, [], None))

count = 0
for email in folders:
    count += 1
    attaches_patch = os.path.join(PATH, email)
    print(count)
    email_sender.send_email(email, SUBJECT, BODY, attaches_patch)

print(f"Всего отправлено: {count} писем")