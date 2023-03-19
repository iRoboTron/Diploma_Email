import textwrap
from PIL import Image, ImageDraw, ImageFont #pip install Pillow

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
             align_center: bool = True):

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

        _font: ImageFont = ImageFont.truetype(font_path, size=font_size)

        for _line in textwrap.wrap(text, width=max_chars):
            _w, _ = self._draw.textsize(_line, font=_font)
            _x = (x_center - _w) / 2
            self._draw.text((_x, y), _line, fill=fill,
                            font=_font, align="center")
            y += _font.getsize(_line)[1]

    def save(self, path:str):
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