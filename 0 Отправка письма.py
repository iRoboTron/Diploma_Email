"""
Postcardware License
Copyright (c) 2023 RoboTron
Email: iAdelfos@gmail.com
https://www.youtube.com/@RoboTron_Channel/
"""

from src import email_sender

email = "iadelfos@gmail.com"

subject = "Конкурс Пятиминутка"

body = """Здравствуйте, %s! 
Приглашаем Вас поучаствовать в нашем конкурсе.
Подробности: https://www.youtube.com/c/RoboTron_Channel
Ждем Ваших работ!
---------------
C уважением команда RoboTron
"""

email_sender.send_email(email, subject, body)