from flask import Blueprint, redirect, url_for 
rgzm = Blueprint('rgzm', __name__)


@rgzm. route("/")
@rgzm. route("/index")
def start():
    return redirect("/menu", code=302)


@rgzm. route("/menu")
def menu():
    return '''
   
<!doctype html>

<html>
 <link rel="stylesheet" href="''' +url_for('static', filename='lab1.css')+'''"
        <head>
         <title>НГТУ, ФБ, Лаборатоорная работа 1</title>
        </head>
        <body>
            <header>
                НГТУ,
ФБ, WEB-программирование, часть 2. 
            </header>
             
            <h2><a href="/rgz" >РГЗ</a></h2>

            <footer>
                &copy; Сердюк Анастасия, ФБИ-11, 3 курс, 2023
            </footer>
        </body>
</html>
'''

