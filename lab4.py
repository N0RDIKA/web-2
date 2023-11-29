from flask import Blueprint,render_template, request, redirect, url_for
lab4 = Blueprint('lab4', __name__)

@lab4.route("/lab4")
def lab():
    return render_template('lab4.html') 

@lab4.route('/lab4/login', methods= ['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'alex' and password == '123':
        return render_template('success.html',username=username)
    else:
        error = 'Неверные логин и/или пароль'
    return render_template ('login.html', error=error, username=username,password=password)



@lab4.route('/lab4/success')
def success():
    username=request.args.get('username')
    return render_template('success.html',username=username,password=password)


@lab4.route('/lab4/frig', methods= ['GET','POST'])
def frig():
    error = ''
    if request.method=='GET':
        return render_template('frig.html', error=error)

    temperature=request.form.get('temperature')

    if temperature == '':
        error = 'Не задана температура'
    else:
        temperature = int(temperature)
        if temperature < -12:
            error = "Не удалось установить температуру, значение слишком низкое "
        elif temperature > -1:
            error = 'Не удалось установить температуру, значение слишком высокое'
        elif (temperature >= -12) and (temperature <= -9):
            error = f'Температура установлена: {temperature}❄️❄️❄️'
        elif (temperature >= -8) and (temperature <= -5):
            error = f'Температура установлена: {temperature}❄️❄️'
        elif (temperature >= -4) and (temperature <= -1):
            error = f'Температура установлена: {temperature}❄️'
    return render_template('frig.html',temperature=temperature, error=error)



@lab4.route('/lab4/zerno', methods= ['GET','POST'])
def zerno():
    if request.method == 'GET':
      return render_template('zerno.html')
    price = 0
    error = ''
    errors= ''
    zerno = request.form.get('zerno')
    weight = request.form.get('weight')

    if weight=='':
        error = "Нужный вес не задан"
        return render_template('zerno.html',error=error)
    weight = int(weight)


    if zerno == 'barley':
        price = 12000 * weight
    elif zerno == 'oats':
        price = 8500 * weight
    elif zerno == 'wheat':
        price = 8700 * weight
    else:
        zerno = 'rye'
        price = 14000 * weight
    if weight <= 0:
        error = "Значение неверно"
        return render_template('zerno.html', error=error)
    elif weight > 500:
        error = "Нужного объема зерна в наличии нет"
        return render_template('zerno.html',error=error)
    elif weight > 50:
        price = price - (price * 10/100)
        errors = "Скидка 10% за большой объем"
    return render_template('zernoOK.html',price=price, zerno=zerno, weight=weight, error=error,errors=errors)

@lab4.route('/lab4/zernoOK')
def zernoOK():
    return render_template('zernoOK.html')    