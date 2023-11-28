from flask import Blueprint, redirect, url_for, render_template, request
lab3 = Blueprint('lab3', __name__)

@lab3. route("lab3/for19/")
def for19(): 
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    num3 = request.args.get('num3')
    return render_template('for19.html', num1 =num1, num2=num2, num3= num3)

@lab3. route("lab3/for199/")
def for199(): 
    different_ordinal = 0
   if num1 == num2 == num3:
    different_ordinal = 4
elif num1 == num2 == num4:
    different_ordinal = 3
elif num1 == num3 == num4:
    different_ordinal = 2
else:
    different_ordinal = 1
    return render_template('for199.html',different_ordinal = different_ordinal )


 
# Determine the ordinal number of the different number
##    different_ordinal = 4
##elif num1 == num2 == num4:
 #   different_ordinal = 3
#elif num1 == num3 == num4:
#   different_ordinal = 2
#else:
   # different_ordinal = 1
   # return render_template('for19.html')