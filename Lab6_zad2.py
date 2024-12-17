print('\nЛабораторная работа 6 задание 2\n')

import sqlite3
from flask import Flask, request, render_template

# обращаемся к БД SQLite
def db():
  ask = sqlite3.connect('NY_2025.db')
  ask.row_factory = sqlite3.Row
  return ask

# конструктор Flask-Application
app = Flask(__name__)
@app.route('/') 
def index():
 x = db()
 frends = x.execute('SELECT * FROM frends').fetchall()
 x.close()
 return render_template('index.html', frends=frends)

# запускаем сайт http://127.0.0.1:5000 в режиме отладки
if __name__ == "__main__":
  app.run(debug=True)
