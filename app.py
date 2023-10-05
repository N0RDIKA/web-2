from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app. route("/")
@app. route("/index")

def start():
    return redirect("/menu", code=302)

@app. route("/menu")
def mrnu():
    return """
<!doctype html>
<html>
        <head>
         <title>НГТУ, ФБ, Лаборатоорная работа 1</title>
        </head>
        <body>
            <header>
                НГТУ,
ФБ, WEB-программирование, часть 2. Список лабораторных
            </header>
             
            <h2><a href="http://127.0.0.1:5000/lab1" >Первая лабораторная</a></h2>

            <footer>
                &copy; Сердюк Анастасия, ФБИ-11, 3 курс, 2023
            </footer>
        </body>
</html>
"""
@app. route("/lab1")
def lab1(): 
    return """
    <!doctype html>
<html>
        <head>
         <title>Сердюк Анастасия Владиславовна, лабораторная  1</title>
        </head>
        <body>
            <header>
                НГТУ, ФБ, Лаборатоорная работа 1
            </header>
             
            <h1>Flask</h1> <h2>— фреймворк для создания веб-приложений на языке
программирования Python, использующий набор инструментов
Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
называемых микрофреймворков — минималистичных каркасов
веб-приложений, сознательно предоставляющих лишь самые базовые возможности.</h2>
 <a href="http://127.0.0.1:5000/menu" >Меню</a>
  <h2>Реализованные роуты </h2>
  <li><a href="http://127.0.0.1:5000/lab1/oak" >Дуб</a></li>
  <li><a href="http://127.0.0.1:5000/lab1/student" >Студент</a></li>
 <li><a href="http://127.0.0.1:5000/lab1/python" >python</a></li>
 <li><a href="http://127.0.0.1:5000/lab1/mars" >Марс</a></li>
            <footer>
                &copy; Сердюк Анастасия, ФБИ-11, 3 курс, 2023
            </footer>
        </body>
</html>
"""
@app. route('/lab1/oak')
def oak(): 
    return '''
    <!doctype html>
<html>
<link rel="stylesheet" href="''' +url_for('static', filename='lab1.css')+'''"
       
        <body>

             
            <h1>Дуб Бардолино натуральный Н1145 ST22</h1> 
            <img  src ="'''+ url_for('static', filename='oakk.jpg' )+'''" height="500 ",  width="500 ">
            <p><b>Размер 3000x655x6 - стеновая панель</p>

<p>Радиус подгиба - R3. </b></p>

 
<p>Серия декоров Дуб Бардолино со следами распила смотрится естественней и имеет более выраженный эффект ручной работы в отличие от классических репродукций дуба. Цветовой оттенок натуральный хорошо подходит к бежевому, серому и коричневому, однако хорошо сочетается и с цветовыми акцентами. Комбинации с белым цветом подчёркивают светлые поры и пользуются особой популярностью в кухне.

Столешницы и стеновые панели  «Форма & Стиль», облицованные бумажно-слоистым пластиком производства EGGER, зарекомендовали себя в качестве идеальной поверхности, подвергающейся интенсивной нагрузке. В пользу таких столешниц говорят как максимальная свобода в реализации дизайнерских идей, так и гигиеничная и простая в уходе поверхность. Используемые в изготовлении столешниц материалы отвечают самым высоким российским и европейским требованиям прочности и экологичности, древесно-стружечные плиты соответствуют классу эмиссии Е1, а пластики отличаются повышенной износостойкостью.
 
В продаже имеется кромка в цвет: 
<li> Кромка с клеем 1500х42х03мм</li>
<li> Кромка с клеем 3000х45х03мм</li></p>
        </body>
</html>
'''

@app. route('/lab1/student')
def  student(): 
    return '''
    <!doctype html>
<html>
<link rel="stylesheet" href="''' +url_for('static', filename='lab1.css')+'''"
       
        <body>
        <p>Сердюк Анастасия Владиславовна, ФБИ-11, 3 курс, 2023 </p>
            <img  src ="'''+ url_for('static', filename='stud.jpg' )+'''" height="250 ",  width="350 ">
           


        </body>
</html>
'''
@app. route('/lab1/python')
def  python(): 
    return '''
    <!doctype html>
<html>


        <link rel="stylesheet" href="''' +url_for('static', filename='lab1.css')+'''"
       
        <body>
          <p>Создатель языка Python — нидерландский программист 
          Гвидо ван Россум. Он был участником проекта по 
          написанию ABC, языка для обучения программированию.
          В конце 1989 года Гвидо приступил к разработке 
          нового языка и задумал его как потомка ABC,
          способного к обработке исключений и взаимодействию
          с операционной системой Amoeba. Так и получился Python.</p>
        
             <img  src ="'''+ url_for('static', filename='p.jpg' )+'''" height="200 ",  width="350 ">
          
          
          <p> Откуда такое название? 
          Многие разработчики считают, 
          что язык назван в честь семейства 
          змей, но это не так. Когда Гвидо 
          работал над проектом, он любил 
          смотреть комедийное шоу «Летающий
           цирк Монти Пайтона», поэтому и 
           нарёк своё творение в честь 
           британской комик-группы. Так 
           что правильно произносить 
           название языка как «Пайтон».</p>
           <p>Python свободно распространялся 
           через интернет и со временем у него 
           появились последователи — люди, 
           заинтересованные в развитии этого
            языка программирования. Первая 
            публикация Python состоялась в 
            феврале 1991 года — это была версия
            0.9.0. В 1994 году Гвидо опубликовал
            Python 1.0, а потом одна за другой
            выпустились и другие версии: до 
            2.0 язык обновился в октябре 2000,
            до 3.0 — в декабре 2008. В октябре
            2021 мир увидела самая свежая версия
            — Python 3.10.0.</p>
            <img  src ="'''+ url_for('static', filename='oip.jpg' )+'''" height="200 ",  width="350 ">
        </body>
</html>
'''

@app. route('/lab1/mars')
def  mars(): 
    return '''
    <!doctype html>
<html>
<link rel="stylesheet" href="''' +url_for('static', filename='lab1.css')+'''"
       
        <body>
        <p> <h2>Марс</h2> всегда пленял людей своей недоступностью и загадочностью. Неведомый мир манил и писателей. Но если англичанин Герберт 
        Уэллс сделал четвёртую планету
        от Солнца местом обитания
        враждебных пришельцев, 
        то Алексей Толстой в 
        своей повести 1937 года
        «Аэлита» создал на Марсе
        подобие земного общества.
        Он же описал прообраз 
        космического корабля для
        полёта к Марсу: 
        яйцеобразный аппарат 
        с реактивной тягой,
        похожий на ракету,
        скорость которого 
        достигала 500 вёрст
        в секунду или около 
        двух миллионов 
        километров в час. С
        такой скоростью при минимальном расстоянии от 
        Земли до Марса 
        в 56 миллионов 
        километров добраться до Красной
        планеты можно за сутки, что
        невозможно даже при нынешних
        технологиях.</p1>
        <p> <img  src ="'''+ url_for('static', filename='mars.jpg' )+'''" height="500 ",  width="500 "></p>

        <p>Mapc, кoнeчнo, мoжeт cтaть втopым дoмoм 
        для чeлoвeчecтвa, нo oн вceгo лишь нeмнoгo
         бoльшe, чeм пoлoвинa Зeмли.
        K пpимepу, Ceвepнaя Aмepикa eдвa пoмeщaeтcя нa oднoй 
        из пoлуcфep плaнeты.</p>
        
        </body>
</html>
'''
@app. route('/lab2/example')
def  example(): 
    name = 'Сердюк Анастасия'
    return render_template('example.html', name=name)
   
