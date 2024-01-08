from PIL import Image, ImageDraw, ImageFont
import textwrap

def create_image_with_text(text, path_to_image, path_to_font):
    import textwrap
    width, height = 900, 900
    background_color = (0, 0, 0)
    # Загрузка изображения
    image = Image.new("RGB", (width, height), background_color)

    # Создание объекта рисования
    draw = ImageDraw.Draw(image)

    # Настройка шрифта
    font_size = 60
    font = ImageFont.truetype(path_to_font, font_size)

    # Определение цвета текста
    text_color = (255, 255, 255)  # Белый цвет (RGB)

    # Разделение текста на строки с автоматическим переносом
    wrapper = textwrap.TextWrapper(width=15)  # Максимальная ширина строки - 20 символов
    text_lines = wrapper.wrap(text)
    bg_color = (255,0,0)

    # Рисование прямоугольника для фона текста
    _, _, line_width, line_height = draw.textbbox((0,0), text, font=font)
    # x = (width - line_width) // 2
    # y = (height - line_height) // 2
    x = 170
    y = 250
    # text_height = line_height * len(text_lines)  # Высота блока текста
    # draw.rectangle((x, y, x + 300, y + text_height), fill=bg_color)

    # Рисование текста
    for line in text_lines:
        draw.text((x, y), line, font=font, fill=text_color)
        y += line_height  # Перемещение на следующую строку

    # Сохранение измененного изображения
    image.save(path_to_image)