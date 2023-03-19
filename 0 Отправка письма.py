"""
Postcardware License
Copyright (c) 2023 RoboTron
Email: iAdelfos@gmail.com
https://www.youtube.com/@RoboTron_Channel/
"""

from src import email_sender

email = "iadelfos@gmail.com"

subject = "Спасибо за программу!"

body = """Здравствуйте, команда RoboTron! 
Это наше первое письмо отправленное через Вашу прогрмму :)
---------------
C уважением!
"""

email_sender.send_email(email, subject, body)