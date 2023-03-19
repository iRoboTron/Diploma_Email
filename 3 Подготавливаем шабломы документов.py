"""
Postcardware License
Copyright (c) 2023 RoboTron
Email: iAdelfos@gmail.com
https://www.youtube.com/@RoboTron_Channel/
"""

from src import diplomas

company = """МБОУ 'Очень при очень длинное название которое существует' в городе Томск """

teacher = "Иванов Владимир Владимирович"
student = "Цыганков Владислав"
position = "за II место получает"


# sertificate = diplomas.create_sertificate(student, company)
# sertificate.save(f"out/Сертификат {student}.png")
# sertificate.show()

descr = company + " В супер крутом соревновании посвещенное всем веселым и смелым ребятам"
diploma = diplomas.create_diploma(position, student, descr)
diploma.save(f"out/Диплом {student}.pdf")
diploma.show()