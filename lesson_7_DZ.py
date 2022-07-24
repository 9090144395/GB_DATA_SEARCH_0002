# как мы обычно скачиваем файлы

import requests

url_capture = 'https://uprostim.com/wp-content/uploads/2021/05/image032-6.jpg'
response = requests.get(url_capture)
with open('cat_capture.jpg', 'wb') as file:
    file.write(response.content)

# Недостаток: все идет неуправляемо через оперативку (сначала весь улетит в оперативку и только потом на диск)
# Недостаток: если такой файл есть он перезапишется (старый файл потеряем)
# Более удобная альтернатива

import wget

url_capture = 'https://uprostim.com/wp-content/uploads/2021/05/image032-6.jpg'
wget.download(url_capture)
# если такой файл уже существует, то новый будет записан рядом (перезаписи не будет)
# сохранение идет через оепративку маленькими частями






# ДЗ -----------------------------------------
# Взять любую категорию товаров на сайте Леруа Мерлен (
# если будет блокировать с 401 ошибкой, возьмите сайт https://www.castorama.ru/). С
#
# обрать следующие данные:
# ● название;
# ● все фото;
# ● ссылка;
# ● цена.
#
# Реализуйте очистку и преобразование данных с помощью ItemLoader.
# Цены должны быть в виде числового значения.
# ---------------------------------------------

# Установка в терминале

# pip install scrapy
# scrapy startproject leroyparser .
# scrapy genspider leroymerlinru leroymerlin.ru