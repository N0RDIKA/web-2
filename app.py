from flask import Flask
app = Flask(__name__)

@app.route("/")
def start():
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
<h1> web-сервер на flask<h1>
<footer>
&copy; Сердюк Анастасия, ФБИ-11, 3 курс, 2023
</footer>
</body>
</html>
"""