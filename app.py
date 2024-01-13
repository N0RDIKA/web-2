from flask import Flask


from ui import ui
from p import p




app = Flask(__name__)
app.secret_key = "123"


app.register_blueprint(ui)
app.register_blueprint(p)







