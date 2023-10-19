from flask import Blueprint, redirect, url_for, render_template, request
lab3 = Blueprint('lab3', __name__)

@lab3. route("/lab3/")
def lab(): 
    return render_template('lab3.html')

@lab3. route('/lab3/forml/')
def  forml(): 
    errors = {}
    user = request.args.get('user')
    if user =='':
        errors['user'] = 'Заполните поле!'
    age = request.args.get('age')
    sex = request.args.get('sex')
    if sex =='':
        errors['sex'] = 'Заполните поле!'
    return render_template('forml.html', user=user, age=age, sex=sex, errors=errors)
   