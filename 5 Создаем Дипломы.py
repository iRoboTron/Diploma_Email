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
COMPANY = "Учебное заведение"
POSITION = "Место"

DIRECTORY = "documents"

count = 0
with open("data/users.csv", encoding='utf8') as r_file:
    file_reader = csv.DictReader(r_file, delimiter=",")
    # Считывание данных из CSV файла
    for row in file_reader:
        if not row[POSITION]:
            continue

        # берем данный для текущего ученика
        _position = f"за {row[POSITION]} место получает:"
        _email = row[EMAIL]
        _student = row[STUDENT]
        _company = row[COMPANY]

        # Создаем папку имя которой почта учителя.
        _directory = f"{DIRECTORY}/{_email}"
        os.makedirs(_directory, exist_ok=True)

        # Создаем и сохраняем Диплом
        diploma = diplomas.create_diploma(_position, _student, _company)
        _path = f"{_directory}/Диплом {row[POSITION]} - {_student}.pdf"
        diploma.save(_path)

        count += 1
print("Всего: ", count)