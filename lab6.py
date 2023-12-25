from flask import Blueprint, render_template, request, redirect
from Db import db
from Db.models import users, articles
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, current_user


lab6 = Blueprint('lab6', __name__)

@lab6.route("/lab6/cheсk")
def main():
    my_users = users.query.all()
    print(my_users)
    return "result in console!"

@lab6.route('/lab6/checkarticles')
def check_articles():
    articles = Article.query.all()
    for article in articles:
        print(f"{article.title}-{article.article_text}")
    return "Articles printed in console"
   
@lab6.route("/lab6/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    username_form = reqquest.form.get("username")
    password_form = reqquest.form.get("password")

    if isUserExist is not None:
        return render_template("register.html")

    hashedPswd = generate_password_hash(password_form, method=hashedPswd)
    db.session.add(newUser)
    db.session.commit()

    return redirect("/lab6/login")

    @lab6.router("/lab6/loginnn", methods = ["GET", "POST"])
    def loginnn():
        if request.method == "GET":
            return render_template("loginnn.html")

        username_form = request.form.get("username")
        password_form = reqquest.form.get("password")

        my_user = users.query.filter_by(username = username_form).first()

        if my_user is not None:
            if check_password_hash(my_user.password, password_form):
                login_user(my_user, remember = False)
                return redirect("/lab6/articles")
        return render_template("loginnn.html")


@lab6.route("/lab6/articless")
@login_required
def article_list():
    my_articles = articles.query.filter_by(user_id = current_user.id).all()
    return render_template("list_articless.html", articles = my_articles)


@lab6.route("/lab6/articless/<string:article_id>")
def getArticle(article_id):
    userID = session.get("id")

    if userID is not None:
        conn = dbConnect()
        cur = conn.cursor()

        cur.execute("SELECT title, article_text FROM articles WHERE id = %s and user_id = %s",(article_id, userID))

        articleBody = cur.fetchone()

        dbClose(cur, conn)

        if articleBody is None:
            return "Not found !"

        text = articleBody[1].splitlines()
        return render_template("articles.html", article_text = text, article_title = articleBody[0], username = session.get("username"))


@lab6.route("/lab6/logout")
@login_required
def logout():
    logout_user()
    return redirect("/lab6")