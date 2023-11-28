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


    error = 'Неверные логин и/или пароль' 
    return render_template ('login.html', error=error, username=username,password=password)



@lab4.route('/lab4/success')
def success():
    username=request.args.get('username')
    return render_template('success.html',username=username)
