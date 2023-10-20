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

@lab3. route('/lab3/order/')
def  order(): 
    return render_template('order.html')

@lab3. route('/lab3/pay/')
def  pay():

    price = 0
    drink = request.args.get('drink')
    if drink == 'coffe':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    if request.args.get('milk') == 'on':
        price+= 30
    if request.args.get('sugar') == 'on':
        price += 10
    return render_template('pay.html', price = price)


@lab3. route('/lab3/succes/')
def  succes():

    return render_template('succes.html')