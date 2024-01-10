from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, render_template, request, redirect, session
import psycopg2

rgz = Blueprint('rgz', __name__)

def dbConnect():
    conn = psycopg2.connect(
        host = "127.0.0.1",
        database="knowledge_base",
        user="serdyuk_anastasiya_knowledge_base",
        password="postgres",
        port=65223
    )
    
    return conn;

def dbClose(cursor, connection):

    cursor.close()
    connection.close()


@rgz.route("/rgz")
def main():
    visibleUser = "username"
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="knowledge_base",
        user="serdyuk_anastasiya_knowledge_base",
        password="postgres",
        port=65223
    )

    cur = conn.cursor()
    cur.execute("SELECT profesia, staj, price_min, price_max FROM articless WHERE status = 'опубликована'")

    results = cur.fetchall()

    cur.close()
    conn.close()

    return render_template('rgz.html', results=results, visibleUser=visibleUser)




@rgz.route('/rgz/register', methods = ["GET", "POST"])
def registerPage():

   
    errors = []
    

    if request.method == "GET":
        return render_template("register.html", errors=errors)


    username = request.form.get("username")
    password = request.form.get("password")

    if not (username or password):
        errors.append("Пожалуйста, заполните все поля")
        print(errors)
        return render_template("register.html", errors=errors)


    hashPassword = generate_password_hash(password, method='pbkdf2')

    conn = dbConnect()
    cur = conn.cursor()

    cur.execute(f"SELECT username FROM users WHERE username = '{username}';")


    if cur.fetchone() is not None:
        errors.append("Пользователь с данным именем уже существует")
        
        conn.close()
        cur.close()
        
        
        return render_template("register.html", errors = errors)
    
    cur.execute(f"INSERT INTO users (username, password) VALUES ('{username}','{hashPassword}');")

    conn.commit()
 
    conn.close()
    cur.close()
    
    return redirect("/rgz/loginn")

@rgz.route('/rgz/loginn', methods = ["GET", "POST"])
def loginnPage():
   

    errors = []

    if request.method == "GET":
        return render_template("loginn.html", errors=errors)

    username=request.form.get("username")
    password = request.form.get("password")

    if not (username or password):
        errors.append("Пожалуйста, заполните все поля")
        return render_template('loginn.html', errors=errors)

    conn = dbConnect()
    cur = conn.cursor()
    

    cur.execute(f"SELECT id, password FROM users WHERE username = '{username}'")


    result = cur.fetchone()

    if result is None:
        errors.append("Неправильный логин или пароль")
        dbClose(cur, conn)
        return render_template("loginn.html", errors=errors)

    userID, hashPassword = result

    if check_password_hash(hashPassword, password):
        session['id'] = userID
        session['username'] = username
        dbClose(cur, conn)
        return redirect("/rgz")

    else:
        errors.append("Неправильный логин или пароль")
        return render_template("loginn.html", errors=errors)


    return redirect("/rgz/loginn")   

@rgz.route('/rgz/cozdzametki', methods=["GET", "POST"])
def cozdzametkiArticle():
    errors=[]
    user_id = session.get("id") 

    if user_id:  
    
        if request.method == "GET":
            return render_template("cozdzametki.html", errors=errors)

        if request.method == "POST":
            profesia = request.form.get("profesia_article")
            staj = request.form.get("staj_article")
            price_min = request.form.get("price_min_article")
            price_max = request.form.get("price_max_article")

            conn = dbConnect()
            cur = conn.cursor()

            cur.execute(f"INSERT INTO articless(user_id, profesia, staj, price_min, price_max) VALUES ({user_id}, '{profesia}', '{staj}', '{price_min}', '{price_max}') RETURNING id")
            new_article_id = cur.fetchone()[0]
            conn.commit()

            dbClose(cur, conn)

            return redirect(f"/rgz/articles/{new_article_id}")
    return redirect("/rgz/loginn")  



@rgz.route("/rgz/articles/<int:article_id>", methods=["GET", "POST"])
def getArticle(article_id):
    if request.method == "POST":
        
        pass
    else:
        user_id = session.get("id") 

        if user_id: 
            conn = dbConnect()
            cur = conn.cursor()

            cur.execute("SELECT profesia, staj , price_min, price_max FROM articless WHERE id = %s AND user_id = %s", (article_id, user_id))
            article_body = cur.fetchone()

            dbClose(cur, conn)

            if article_body is None:
                return "Article not found!"

            
            return render_template("article.html", profesia=article_body[0], staj=article_body[1], price_min=article_body[2], price_max=article_body[3])

        return redirect("/rgz/loginn")


@rgz.route("/rgz/articles")
def getArticleALL():  
    user_id = session.get("id")
    
    if user_id is not None:  
        conn = dbConnect()
        cur = conn.cursor()

        cur.execute("SELECT id, profesia, staj , price_min, price_max FROM articless where user_id = %s", (user_id,))
        articles = cur.fetchall() 

        dbClose(cur, conn)

        if articles is None:  
            return "No articles found!"
        
        return render_template("articles.html", articles=articles, username=session.get("username"))  # Passing all articles to the template

    return redirect("/rgz/loginn")



@rgz.route('/rgz/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect("/rgz/loginn")

 
@rgz.route("/rgz/delete/<int:article_id>", methods=["POST"])
def delete_record(article_id):
    if request.method == "POST":
        user_id = session.get("id")

        if user_id is not None:  
            conn = dbConnect()
            cur = conn.cursor()
            cur.execute("DELETE FROM articless WHERE id = %s AND user_id = %s", (article_id, user_id))
            conn.commit()  
            dbClose(cur, conn)
            
            return "Успех"  

    return "Неавторизованный"  




@rgz.route("/rgz/hide_article/<int:article_id>", methods=["POST"])
def hide_article(article_id):
    user_id = session.get("id")

    if user_id is not None:
        conn = dbConnect()
        cur = conn.cursor()

        
        cur.execute("SELECT * FROM articless WHERE id = %s AND user_id = %s", (article_id, user_id))
        article = cur.fetchone()

        if article:  
           
            cur.execute("UPDATE articless SET status = 'скрыто' WHERE id = %s", (article_id,))
            conn.commit()  
            dbClose(cur, conn)
            return "Статья успешно скрыта"
        else:
            dbClose(cur, conn)
            return "Статья не найдена или у вас нет прав для изменения статуса"
    else:
        return "Вы не авторизованы"

    return "Произошла ошибка"



@rgz.route("/rgz/publish_article/<int:article_id>", methods=["POST"])
def publish_article(article_id):
    user_id = session.get("id")

    if user_id is not None:
        conn = dbConnect()
        cur = conn.cursor()

        
        cur.execute("SELECT * FROM articless WHERE id = %s AND user_id = %s", (article_id, user_id))
        article = cur.fetchone()

        if article:  
           
            cur.execute("UPDATE articless SET status = 'опубликована' WHERE id = %s", (article_id,))
            conn.commit()  
            dbClose(cur, conn)
            return "Статья успешно скрыта"
        else:
            dbClose(cur, conn)
            return "Статья не найдена или у вас нет прав для изменения статуса"
    else:
        return "Вы не авторизованы"

    return "Произошла ошибка"

@rgz.route('/rgz/edit_article/<int:article_id>', methods=["GET", "POST"])
def editArticle(article_id):
    if request.method == "POST":
        new_profesia = request.form.get("newProfesia")
        new_staj = request.form.get("newStaj")
        new_price_min = request.form.get("newPriceMin")
        new_price_max = request.form.get("newPriceMax")

        conn = dbConnect()
        cur = conn.cursor()

        cur.execute(f"UPDATE articless SET profesia = '{new_profesia}', staj = '{new_staj}', price_min = {new_price_min}, price_max = {new_price_max} WHERE id = {article_id}")
        conn.commit()

        dbClose(cur, conn)

        return redirect(f"/rgz/articles/{article_id}")
    else:
       
        return render_template('edit_article.html', article_id=article_id, newProfesia="новая_профессия", newStaj="новый_стаж", newPriceMin=0, newPriceMax=200000000000) 


@rgz.route("/rgz/search_prof")
def searchprof():
    return render_template('search.html')



@rgz.route("/rgz/search_by_profession", methods=["GET"])
def search_by_profession():
    profesia = request.args.get("profesia")


    conn = dbConnect()  
    cur = conn.cursor()

    if profesia:
        cur.execute("SELECT profesia, staj, price_min, price_max FROM articless WHERE profesia = %s and status = 'опубликована'", (profesia, ))
        search_results = cur.fetchall()
        dbClose(cur, conn)  

        return render_template("profession.html", search_results=search_results, profesia=profesia)
    else:
        return "Не найдено."


@rgz.route("/rgz/search_by_staj", methods=["GET"])
def search_by_staj():
    min_staj = request.args.get("min_staj")
    max_staj = request.args.get("max_staj")

    conn = dbConnect()
    cur = conn.cursor()

    if min_staj and max_staj:
        cur.execute("SELECT profesia, staj, price_min, price_max FROM articless WHERE staj BETWEEN %s AND %s AND status = 'опубликована'", (min_staj, max_staj))
        search_results = cur.fetchall()
        dbClose(cur, conn)

        return render_template("staj.html", search_results=search_results, min_staj=min_staj, max_staj=max_staj)
    else:
        return "Не найдено."


@rgz.route('/rgz/searchstaj')
def searchbystaj():
    return render_template('search_by_staj.html')



@rgz.route('/rgz/searchbyprice')
def searchbyprice():
    return render_template('search_by_price.html')

@rgz.route("/rgz/search_by_price", methods=["GET"])
def search_by_price():
    min_price = request.args.get("min_price")
    max_price = request.args.get("max_price")

    conn = dbConnect()
    cur = conn.cursor()

    if min_price and max_price:
        cur.execute("SELECT profesia, staj, price_min, price_max FROM articless WHERE price_min BETWEEN %s AND %s and price_max BETWEEN %s AND %s AND status = 'опубликована'", (min_price, max_price, min_price, max_price))
        search_results = cur.fetchall()
        dbClose(cur, conn)

        return render_template("price.html", search_results=search_results, min_price=min_price, max_price=max_price)  # Название шаблона должно быть указано здесь

    else:
        return "Не найдено."


@rgz.route('/rgz/search_form')
def search():
    return render_template('search_form.html')