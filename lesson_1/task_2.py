"""
Выполнение практических заданий к уроку №1 Python-start.
Студент: Максим Сапунов Jenny6199@yandex.ru

Задача №2. Пользователь вводит время в секундах. Переведите время в часы,
минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование
строк.
"""
print('Форматирование введенного времени: ')
divide_time = int(input('Введите время в секундах: '))
hours = '%02d' % (divide_time // 3600)
divide_time = divide_time % 3600
minutes = '%02d' % (divide_time // 60)
divide_time = divide_time % 60
seconds = '%02d' % (divide_time % 60)

result = f'Данному количеству секунд соответствует: чч:мм:сс - {hours}:{minutes}:{seconds}'
print(result)
