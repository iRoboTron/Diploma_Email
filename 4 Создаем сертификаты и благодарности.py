"""
Postcardware License
Copyright (c) 2023 RoboTron
Email: iAdelfos@gmail.com
https://www.youtube.com/@RoboTron_Channel/
"""

import csv
import os

from src import diplomas

EMAIL = "E-mail"
STUDENT = "Участник"
TEACHER = "ФИО учителя"
COMPANY = "Учебное заведение"

DIRECTORY = "out"

with open("data/users.csv") as r_file:
    # Создаем объект DictReader, указываем символ-разделитель ","
    file_reader = csv.DictReader(r_file, delimiter=";")
    # Считывание данных из CSV файла
    for row in file_reader:
        # берем данный для текущего ученика
        _email = row[EMAIL]
        _student = row[STUDENT]
        _company = row[COMPANY]

        # Создаем папку имя которой почта учителя.
        _directory = f"{DIRECTORY}/{_email}"
        os.makedirs(_directory, exist_ok=True)

        # Создаем и сохраняем Сертифика
        sertificate = diplomas.create_sertificate(_student, _company)
        _path = f"{_directory}/Сертификат - {_student}.jpg"
        sertificate.save(_path)