"""
Postcardware License
Copyright (c) 2023 RoboTron
Email: iAdelfos@gmail.com
https://www.youtube.com/@RoboTron_Channel/
"""

import textwrap
from PIL import Image, ImageDraw, ImageFont  # pip install Pillow


class DiplomaBase:

    def __init__(self, path):
        self._path = path  # ссылка на исходную картинку
        self._image = Image.open(path)
        self._draw = ImageDraw.Draw(self._image)

    def text(self, text: str,
             x: int,
             y: int,
             font_path: str,
             font_size: int,
             max_width: int,
             fill: str = "black",
             align_center: bool = True) -> None:
        """
        Вставка однострочного текста
        :param text: Текст для вставки
        :param x: Отступ в пикселях от левого края (при align_center=True, x - обозначает середину)
        :param y: Отступ в пикселях от верхнего края
        :param font_path: Месторасположение шрифта использувоемого для текста
        :param font_size: Размер шрифта
        :param max_width: Максимальная ширина в пикселях
        :param fill: Цвет текста
        :param align_center: Использовать выравнивание по середение (по умолчанию выравнивание по левому краю

        Examples:
            >>> template.text("Иванов Иван", 300, 1150, "./fonts/Times New Roman.ttf", 90, 1500)

        """
        _font = self._get_font(text, font_path, (font_size - 5), max_width)
        _w, _ = self._draw.textsize(text, font=_font)
        _x = x
        if align_center:
            _x = (x - _w) / 2

        self._draw.text((_x, y), text, fill=fill, font=_font)

    def multi_line(self, text: str,
                   x_center: int,
                   y: int,
                   font_path: str,
                   font_size: int,
                   max_chars: int,  # Максимальное количество символов в строке
                   fill: str = "black") -> None:
        """
        **Вставка многострочного текста.**
        ОСТОРОЖНО, если текст содержит символ тильда "~" то она заменится на перенос текста на новую строку

        :param text: Текст для вставки
        :param x_center: Нахождение середины текста в пикселях от левого края
        :param y: Отступ в пикселях от верхнего края
        :param font_path: Месторасположение шрифта использувоемого для текста
        :param font_size: Размер шрифта
        :param max_chars: Максималоно допустимое количество символов в одной строчке
        :param fill: Цвет текста
        """
        _font: ImageFont = ImageFont.truetype(font_path, size=font_size)

        def write_line(_line_w, y):
            _w, _ = self._draw.textsize(_line_w, font=_font)
            _x = (x_center - _w) / 2
            self._draw.text((_x, y), _line_w, fill=fill,
                            font=_font, align="center")
            y = _font.getsize(_line_w)[1]
            return y

        for _line in textwrap.wrap(text, width=max_chars):
            for _sub_line in _line.split('~'):
                y += write_line(_sub_line, y)

    def save(self, path: str):
        self._image.save(path)
        print(path)

    def show(self):
        self._image.show()

    def _get_font(self, text: str, font_path: str,
                  font_size: int, max_width: int = 30) -> ImageFont:
        _font: ImageFont = ImageFont.truetype(font_path, size=font_size)
        _w, _ = self._draw.textsize(text, font=_font)

        if _w > max_width:
            # создаем новый вариант с уменьшенным размером шрифта
            return self._get_font(text, font_path, (font_size - 5), max_width)
        return _font


if __name__ == "__main__":
    pass
