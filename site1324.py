from flask import Flask, render_template, url_for, redirect, request, jsonify
import sqlite3
from flask import g
app = Flask(__name__)
DATABASE1 = 'C:\Программирование\PYCHARM projects\MyProject№1\db1.db'
def get_db1():
    db = getattr(g, 'database1', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE1)
    return db
DATABASE2 = 'C:\Программирование\PYCHARM projects\MyProject№1\db2.db'
def get_db2():
    db = getattr(g, 'database2', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE2)
    return db
DATABASE3 = 'C:\Программирование\PYCHARM projects\MyProject№1\db3.db'
def get_db3():
    db = getattr(g, 'database3', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE3)
    return db
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, 'database1', None)
    if db is not None:
        db.close()
    db = getattr(g, 'database2', None)
    if db is not None:
        db.close()
    db = getattr(g, 'database3', None)
    if db is not None:
        db.close()
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('Mainhakaton.html')
    if request.method == 'POST':
        data1 = request.form['log']
        if data1 =='Поливальная машина№1':
            return redirect(url_for('info1'))
        elif data1 =='Поливальная машина№2':
            return redirect(url_for('info2'))
        elif data1 =='Поливальная машина№3':
            return redirect(url_for('info3'))
@app.route('/info1')
def info1():
    conn = get_db1()
    cursor = conn.cursor()
    work1=eval(cursor.execute(f"SELECT Watering FROM Work  order by Watering desc LIMIT 1;").fetchone()[0])
    work2=eval(cursor.execute(f"SELECT Working FROM Work  order by Watering desc LIMIT 1;").fetchone()[0])
    if work1==True and work2==True:
        return render_template('Полив. машина№1.html', conditions='Нормальная работа')
    else:
        return render_template('Полив. машина№1.html', conditions='Ошибка в работе')
@app.route('/info2')
def info2():
    conn = get_db2()
    cursor = conn.cursor()
    work1=eval(cursor.execute(f"SELECT Watering FROM Work2  order by Watering desc LIMIT 1;").fetchone()[0])
    work2=eval(cursor.execute(f"SELECT Working FROM Work2  order by Watering desc LIMIT 1;").fetchone()[0])
    if work1==True and work2==True:
        return render_template('Полив. машина№2.html', conditions='Нормальная работа')
    else:
        return render_template('Полив. машина№2.html', conditions='Ошибка в работе')
@app.route('/info3')
def info3():
    conn = get_db3()
    cursor = conn.cursor()
    work1=eval(cursor.execute(f"SELECT Watering FROM Work3  order by Watering desc LIMIT 1;").fetchone()[0])
    work2=eval(cursor.execute(f"SELECT Working FROM Work3  order by Watering desc LIMIT 1;").fetchone()[0])
    if work1==True and work2==True:
        return render_template('Полив. машина№3.html', conditions='Нормальная работа')
    else:
        return render_template('Полив. машина№3.html', conditions='Ошибка в работе')
if __name__ == '__main__':
    app.run(host='0.0.0.0')