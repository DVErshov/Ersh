print('\nЛабораторная работа 6 задание 1\n')
import sqlite3 

# Создаем подключение к базе данных, при этом будет создан файл NY_2025.db 
connection = sqlite3.connect('NY_2025.db')
ask = connection.cursor()

# Создаем таблицу Frends
ask.execute('''
  CREATE TABLE IF NOT EXISTS Frends (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  prb TEXT NOT NULL,
  prc TEXT NOT NULL,
  st REAL )
  ''')

# добавляем данные в таблицу
add_frend = lambda id, name, prb, prc, st: ask.execute('INSERT INTO Frends (id, name, prb, prc, st) VALUES (?, ?, ?, ?, ?)', (id, name, prb, prc, st))

add_frend(1, 'Свинки', 'плед серый + ДМ серый', 'остановка макет', 0.5)
add_frend(2, 'Шевченки', 'плед красный + ДМ красный', '', 1)
add_frend(3, 'Ксюньки', 'плед красный + ДМ красный', 'шапка + игрушка', 1)
add_frend(4, 'Светик', 'плед серый + ДМ серый', 'карандаши акварель', 1)
add_frend(5, 'Сыровары', 'плед домики + светильник', '', 0)
add_frend(6, 'Сестры', 'плед красный + носки', 'гномы комплект', 1)
add_frend(7, 'Дочь старшая', 'плед красный + чай', 'игра + набор доктор', 0.5)
add_frend(8, 'Дочь младшая', 'плед серый + ДМ серый', '', 1)
add_frend(9, 'Костики', 'плед красный', 'гномы комплект', 0)
add_frend(10, 'Полина', 'плед серый + гном серый', '', 1)
add_frend(11, 'Бодровы', 'плед серый + гном красный', '', 1)
add_frend(12, 'Тетя Галя', 'чай + икра красная', '', 0)

# Проверяем есть ли записи в таблице
ask.execute('SELECT * FROM Frends')
fr = ask.fetchall()
for i in fr:
  print(i)

# сохраняем данные и закрываем базу данных
connection.commit()
connection.close()


