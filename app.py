from flask import Flask, redirect, url_for, render_template
from lab1 import lab1
app = Flask(__name__)
app.register_blueprint(lab1)



@app.route('/lab2/example')
def  example(): 
    name = 'Сердюк Анастасия'
    number = '2'
    group = 'ФБИ-11'
    numbercurs = '3'
    fruits = [
        {'name':'яблоки', 'price': 100},
        {'name':'груши', 'price': 120},
        {'name':'апельсины', 'price': 80},
        {'name':'мандарины', 'price': 95},
        {'name':'манго', 'price': 321}
        ]
    book = [
        {'books': 'Тринадцатая сказка', 'str':  420, 'ganr':'Современная зарубежная литература','avtor': 'Диана Сеттерфилд'},
        {'books': 'Вторая жизнь Уве', 'str':  550, 'ganr':'Современная зарубежная литература','avtor': 'Фредрик Бакман'},
        {'books': 'Игра престолов', 'str':  875, 'ganr':'Зарубежное фэнтези','avtor': 'Джордж Мартин'},
        {'books': 'Цветы для Элджернона', 'str':  213, 'ganr':'Научная фантастика','avtor': 'Дэниел Киз'},
        {'books': 'Не отпускай меня', 'str':  275, 'ganr':'Современная зарубежная литература','avtor': 'Кадзуо Исигуро'},
        {'books': 'Чтец', 'str':  125, 'ganr':'Современная зарубежная литература','avtor': 'Бернхард Шлинк'},
        {'books': 'Книжный вор', 'str':  353, 'ganr':'Современная зарубежная литература','avtor': 'Маркус Зусак'},
        {'books': 'С жизнью наедине', 'str':  403, 'ganr':'Современная зарубежная литература','avtor': 'Кристин Ханна'},
        {'books': 'Не такая, как все', 'str':  186, 'ganr':'Современная зарубежная литература','avtor': 'Марк Леви'},
        {'books': 'Соловей', 'str':  369, 'ganr':'Современная зарубежная литература','avtor': 'Кристин Ханна'}
    ]
    return render_template('example.html', name=name, number = number, group=group, numbercurs=numbercurs, fruits = fruits, book = book)
   
@app.route('/lab2/')
def  lab2(): 
    return render_template('lab2.html')

@app.route('/lab2/lab22/')
def  lab22(): 
    return render_template('lab2_2.html')



@app.route('/lab2/lab22/flower/')
def  flower(): 
    return render_template('lab_flower.html')



@app.route('/lab2/lab22/berry/')
def  berry(): 
    return render_template('lab_berry.html')



@app.route('/lab2/lab22/car/')
def  car(): 
    return render_template('lab_car.html')




@app.route('/lab2/lab22/painting/')
def  painting(): 
    return render_template('lab_painting.html')




@app.route('/lab2/lab22/furniture/')
def  furniture(): 
  return render_template('lab_furniture.html')
  


