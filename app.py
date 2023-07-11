import os

# import src.fetch_dailymanu as fetch_d #編集画面に書き戻す
# import src.fetch_menu as fetch_c #編集画面に書き戻す
# import src.send_dailymenu as send_d #デイリーメニューのファイルを送る
# import src.send_editeddailymenu as send_edd # 編集したデータを反映させる
# import src.send_editedmenu as send_edc #編集したデータを反映させる
# import src.update_soldout as update_soldout #売り切れを送る

from flask import Flask
from flask_login import UserMixin, LoginManager, login_user, logout_user, login_required
from flask import render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
# from datetime import datetime
# import pytz
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://team6:9RgBGqgc@localhost/team6db'
app.config['SECRET_KEY'] = os.urandom(24)
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

class menu(db.Model):
    menu_id = db.Column(db.String, unique=True, nullable=False, primary_key=True)
    menu_name = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    energy = db.Column(db.Float, nullable=False, default=0)
    protein = db.Column(db.Float, nullable=False, default=0)
    lipid = db.Column(db.Float, nullable=False, default=0)
    carbohydrates = db.Column(db.Float, nullable=False, default=0)
    salt = db.Column(db.Float, nullable=False, default=0)
    wheat = db.Column(db.Boolean, nullable=False, default=False)
    egg = db.Column(db.Boolean, nullable=False, default=False)
    milk = db.Column(db.Boolean, nullable=False, default=False)
    buckwheat = db.Column(db.Boolean, nullable=False, default=False)
    peanut = db.Column(db.Boolean, nullable=False, default=False)
    shrimp = db.Column(db.Boolean, nullable=False, default=False)
    crab = db.Column(db.Boolean, nullable=False, default=False)
    soldout = db.Column(db.Boolean, nullable=False, default=False)

class dailymenu_a(db.Model):
    menu_date = db.Column(db.DateTime(8), nullable=False)
    menu_name = db.Column(db.String(40), nullable=False, primary_key=True)
    energy = db.Column(db.Float(3), nullable=False, default=0)
    protein = db.Column(db.Float(3), nullable=False, default=0)
    lipid = db.Column(db.Float(3), nullable=False, default=0)
    carbohydrates = db.Column(db.Float(4), nullable=False, default=0)
    salt = db.Column(db.Float(3), nullable=False, default=0)
    wheat = db.Column(db.Boolean, nullable=False, default=False)
    egg = db.Column(db.Boolean, nullable=False, default=False)
    milk = db.Column(db.Boolean, nullable=False, default=False)
    buckwheat = db.Column(db.Boolean, nullable=False, default=False)
    peanut = db.Column(db.Boolean, nullable=False, default=False)
    shrimp = db.Column(db.Boolean, nullable=False, default=False)
    crab = db.Column(db.Boolean, nullable=False, default=False)

class dailymenu_b(db.Model):
    menu_date = db.Column(db.DateTime(8), nullable=False, primary_key=True)
    menu_name = db.Column(db.String(40), nullable=False)
    energy = db.Column(db.Float(3), nullable=False, default=0)
    protein = db.Column(db.Float(3), nullable=False, default=0)
    lipid = db.Column(db.Float(3), nullable=False, default=0)
    carbohydrates = db.Column(db.Float(4), nullable=False, default=0)
    salt = db.Column(db.Float(3), nullable=False, default=0)
    wheat = db.Column(db.Boolean, nullable=False, default=False)
    egg = db.Column(db.Boolean, nullable=False, default=False)
    milk = db.Column(db.Boolean, nullable=False, default=False)
    buckwheat = db.Column(db.Boolean, nullable=False, default=False)
    peanut = db.Column(db.Boolean, nullable=False, default=False)
    shrimp = db.Column(db.Boolean, nullable=False, default=False)
    crab = db.Column(db.Boolean, nullable=False, default=False)

class soldout(db.Model):
    menu_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    soldout = db.Column(db.Boolean, nullable=False, default=True)

class userdata(UserMixin, db.Model):
    uid = db.Column(db.Integer, unique=True, primary_key=True)
    uname = db.Column(db.String(30), unique=True, nullable=False)
    upass = db.Column(db.String(32), nullable=False)

@app.route('/')
def constmenu():
    menulists = menu.query.all()
    # menulists = db.session.query(menu).all()
    return render_template('index.html', menulists=menulists)

@app.route('/mngtop')
#@login_required
def mngtop():
    return render_template('mngmnt.html')

@app.route('/dailymng')
#@login_required
def dailymng():
    return render_template('daily.html')

@app.route('/constmng')
#@login_required
def constmng():
    return render_template('constant.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        uname = request.form.get('username')
        upass = request.form.get('password')
        user = userdata.query.filter_by(uname=uname).first()
        if upass == user.upass: #check_password_hash(user.upass, upass):
            login_user(user)
            return redirect('/') # ログインが成功したらrootに戻る
        else:
            return redirect('/login')
    else:
        return render_template('login.html')

@app.route('/logout')
#@login_required
def logout():
    logout_user()
    return redirect('/login') # ログアウトしたらログイン画面に戻る

@login_manager.user_loader
def load_user(user_id):
    return userdata.query.get(int(user_id))

#Pythonファイル呼び出し 

# @app.route('/fetch_d')
# def fetch_d():
#     return fetch_d.fetch_dailymenu()

# @app.route('/fetch_c')
# def fetch_c():
#     return fetch_c.fetch_menu()

# @app.route('/send_d')
# def send_d():
#     return send_d.send_dailymenu()

# @app.route('/send_edd')
# def send_edd():
#     return send_edd.send_editeddailymenu()

# @app.route('/send_edc')
# def send_edc():
#     return send_edc.send_editedmenu()

# @app.route('/update_soldout')
# def update_soldout():
#     return update_soldout.update_soldout()

if __name__ == "__main__":
    app.run(debug=True,host='172.16.16.7',port=8086,threaded=True)
