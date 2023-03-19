"""
Postcardware License
Copyright (c) 2023 RoboTron
Email: iAdelfos@gmail.com
https://www.youtube.com/@RoboTron_Channel/
"""
import csv

from src import email_sender

PATH_TO_CSV = "data/Invite.csv"
EMAIL = "Емайл"
USER = "ФИО"
ENCODING = 'Windows-1251' # 'Windows-1251' or 'utf8'
DELIMITER = ";"  # указываем символ-разделитель "," ";"

SUBJECT = "Конкурс Пятиминутка"
BODY = """Здравствуйте, %s! 
Приглашаем Вас поучаствовать в нашем конкурсе.
Подробности: https://www.youtube.com/c/RoboTron_Channel
Ждем Ваших работ!
---------------
C уважением команда RoboTron
"""

with open(PATH_TO_CSV, encoding=ENCODING) as r_file:
    file_reader = csv.DictReader(r_file, delimiter=DELIMITER)
    for row in file_reader:
        print(row)
        _email = row[EMAIL]
        _user = row[USER]
        _body = BODY % (_user)

        email_sender.send_email(_email, SUBJECT, _body)