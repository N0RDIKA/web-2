from flask import Flask, redirect
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

            <footer>
                &copy; Сердюк Анастасия, ФБИ-11, 3 курс, 2023
            </footer>
        </body>
</html>
"""