from src.diploma_base import DiplomaBase

# шрифты
TIMES_NEW_ROMAN = 'data/fonts/Times New Roman.ttf'
TIMES_NEW_ROMAN_BOLD = 'data/fonts/Times New Roman Bold.ttf'
LOBSTER_REGULAR = 'data/fonts/Lobster-Regular.ttf'



def create_sertificate(student, company):
    """Шаблом для создания """
    template = DiplomaBase("data/imgs/Sert.jpg")
    x = 300
    # company = company.upper() # Большими буквами
    template.text(student, x=x, y=730, font_path=LOBSTER_REGULAR, font_size=140, max_width=1700, fill="#ff0000",align_center=False)
    template.multi_line(company, 2400, y=950, font_path=TIMES_NEW_ROMAN, font_size=60, max_chars=50, fill="#ff0000")

    return template


def create_diploma(position, student, company):
    """Шаблом для создания Диплома """
    template = DiplomaBase("data/imgs/Dipl.jpg")
    x = 2200
    company = company.upper() # Большими буквами
    template.text(position, x=x, y=1150, font_path=TIMES_NEW_ROMAN, font_size=90, max_width=1500)
    # template.text(nomination, x=x, y=1300, font_path=TIMES_NEW_ROMAN, font_size=80, max_width=1700)

    template.text(student, x=x, y=1250, font_path=LOBSTER_REGULAR, font_size=200, max_width=1700, fill="#FF0000")

    template.multi_line(company, x, y=1650, font_path=TIMES_NEW_ROMAN, font_size=60, max_chars=50, )
    # template.text(id, x=x, y=3250, font_path=TIMES_NEW_ROMAN, font_size=60, max_width=1400, fill="#FFFFFF")


    return template


if __name__ == "__main__":
    pass
