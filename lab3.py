from flask import Blueprint, redirect, url_for, render_template, request
import math
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
    if age =='':
        errors['age'] = 'Заполните поле!'
    sex = request.args.get('sex')
    
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

@lab3. route('/lab3/gb/')
def  gb(): 
    errors = {}
    gb = request.args.get('gb')
    if gb =='':
        errors['gb'] = 'Заполните поле!'
    gbb = request.args.get('gbb')
    if gbb =='':
        errors['gbb'] = 'Заполните поле!'
    gbbb = request.args.get('gbbb')
    if gbbb =='':
        errors['gbbb'] = 'Заполните поле!'
    tip = request.args.get('tip')
    polkav = request.args.get('polkav')
    
    polkab = request.args.get('polkab')
   
    bagaj = request.args.get('bagaj') 
    
    pynktv = request.args.get('pynktv')
    if pynktv =='':
        errors['pynktv'] = 'Заполните поле!'
    pynktp = request.args.get('pynktp')
    if pynktp =='':
        errors['pynktp'] = 'Заполните поле!'
        
    age = request.args.get('age')
    if age =='':
        errors['age'] = 'Заполните поле!'
    date = request.args.get('date')
    if date =='':
        errors['date'] = 'Заполните поле!'
    return render_template('gb.html',gb = gb, gbb=gbb, gbbb=gbbb, errors=errors, tip = tip, polkav=polkav, polkab=polkab, bagaj=bagaj, age = age, date=date, pynktp=pynktp, pynktv=pynktv)
    



@lab3. route("/lab3/for199/<int:num1>/<int:num2>/<int:num3>/<int:num4>")
def for199(num1,num2,num3,num4): 
    if num1a == num2b == num3c == num4d:
        result = 4
    elif num1a == num2b == num4d:
        result = 3
    elif num1a == num3c == num4d:
        result = 2
    else:
        result = 1
    return f"{result}"


    
   
@lab3. route("/lab3/for19/<float:x>/<int:n>")
def for19(x,n):
    result = 0.0
    f=1
    if n <= 0:
        return "должно быть больше 0"
    for i in range(1,n + 1):
        a= (f * x **(2 * i - 1))/math.factorial(2 * i - 1)
        result += a
        f *= -1
    return f"приближение значение sin({x}) c {n}: {result}"
    

