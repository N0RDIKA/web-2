from flask import Flask

from rgz import rgz
from rgzm import rgzm





app = Flask(__name__)
app.secret_key = "123"

app.register_blueprint(rgz)
app.register_blueprint(rgzm)








