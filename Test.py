from PIL import Image
import os

def find_first_non_empty_pixel(image):
    width, height = image.size
    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            if pixel[3] != 0:  # Не прозрачный пиксель
                return x, y
    return None

def crop_animation_frames(input_path, output_folder):
    # Открытие изображения
    img = Image.open(input_path)

    # Находим координаты первого непустого пикселя
    first_pixel = find_first_non_empty_pixel(img)

    if first_pixel is None:
        print("Изображение полностью прозрачно.")
        return

    # Получение размеров изображения
    width, height = img.size

    left_bound, top_bound = first_pixel
    right_bound = width
    bottom_bound = height

    # Определение границ обрезки
    for x in range(first_pixel[0], width):
        column = [img.getpixel((x, y))[3] for y in range(height)]
        if any(column):
            right_bound = x
            break

    for y in range(first_pixel[1], height):
        row = [img.getpixel((x, y))[3] for x in range(width)]
        if any(row):
            bottom_bound = y
            break

    # Печать границ для отладки
    print(f"Left: {left_bound}, Right: {right_bound}, Top: {top_bound}, Bottom: {bottom_bound}")

    # Создание папки для сохранения обрезанного изображения
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Обрезка изображения и сохранение
    cropped_img = img.crop((left_bound, top_bound, right_bound, bottom_bound))
    output_path = os.path.join(output_folder, "cropped_animation.png")
    cropped_img.save(output_path)

    print(f"Обрезанное изображение сохранено в: {output_path}")


crop_animation_frames('data/Sprites/main_character_sprite/hesh/frame_0_0.png', 'data/test_folser')