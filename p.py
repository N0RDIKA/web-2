from flask import Blueprint, render_template, request, redirect, session


p = Blueprint('p', __name__)



@p.route("/1")
def main():

    return render_template('o.html')

@p.route("/1/pp")
def pp():
    return render_template("11.html")
    

@p.route("/1/pp/calculate", methods=['GET'])
def p111():
    one = request.args.get("one")
    two = request.args.get("two")
    three = request.args.get("three")
    fo = request.args.get("fo")
    thi = request.args.get("thi")
    

    if not (one and two and three and fo and thi):
        return "Ошибка: заполнете все поля"


    if not (one.isdigit() and two.isdigit() and three.isdigit()):
        return "Ошибка: введите все поля"

    one = int(one)
    two = int(two)
    three = int(three)
    fo = int(fo)
    thi = int(thi)

    numbers = [one, two, three, fo, thi]

    numbers.sort(reverse=True)


    result = numbers[:2]

    return render_template("111.html", result=result)
