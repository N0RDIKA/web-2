from flask import Blueprint, redirect, url_for 
ui = Blueprint('ui', __name__)


@ui. route("/")
@ui. route("/index")
def start():
    return redirect("/menu", code=302)


@ui. route("/menu")
def menu():
    return '''
   
<!doctype html>

<html>
 <link rel="stylesheet" href="''' +url_for('static', filename='lab1.css')+'''"
        <head>
         <title></title>
        </head>
        <body>
            <header> 
            </header>
             

            <h2><a href="/1" >p</a></h2>

            <footer>
                
            </footer>
        </body>
</html>
'''

