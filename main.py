from flask import Flask, render_template, request, redirect, flash
import pymysql

app = Flask('__name__')
app.secret_key = "Secret Key"


@app.route('/')
def index():
    try:
        db = pymysql.connect(host="localhost", user="root", password="Mysql@123", database="manage_employee")
        cu = db.cursor()
        q = "select * from employee"
        cu.execute(q)
        data = cu.fetchall()
        return render_template("dashboard.html", d=data)

    except Exception as e:
        print("Error:")


@app.route('/create')
def create():
    return render_template("form.html")


@app.route('/store', methods=['POST'])
def store():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']

    try:
        db = pymysql.connect(host="localhost", user="root", password="Mysql@123", database="manage_employee")
        cu = db.cursor()
        q = "insert into employee (name,email,phone) values('{}','{}','{}')".format(name, email, phone)
        cu.execute(q)
        db.commit()
        flash("Record inserted successfully")
        return redirect('/')

    except Exception as e:
        return "Error: ", e


@app.route('/delete/<rid>')
def delete(rid):
    try:
        db = pymysql.connect(host="localhost", user="root", password="Mysql@123", database="manage_employee")
        cu = db.cursor()
        q = f"delete from employee where id='{rid}'"
        cu.execute(q)
        db.commit()
        flash("Record deleted successfully")
        return redirect('/')

    except Exception as e:
        return "Error: ", e


@app.route('/edit/<rid>')
def edit(rid):
    try:
        db = pymysql.connect(host="localhost", user="root", password="Mysql@123", database="manage_employee")
        cu = db.cursor()
        q = "select * from employee where id='{}'".format(rid)
        cu.execute(q)
        data = cu.fetchone()
        return render_template('editform.html', d=data)

    except Exception as e:
        return "Error: ", e


@app.route('/update/<rid>', methods=['POST'])
def update(rid):
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    try:
        db = pymysql.connect(host="localhost", user="root", password="Mysql@123", database="manage_employee")
        cu = db.cursor()
        q = "update employee set name='{}', email='{}', phone='{}' where id='{}'".format(name, email, phone, rid)
        cu.execute(q)
        db.commit()
        flash("Record updated successfully")
        return redirect('/')

    except Exception as e:
        return "Error: ", e


app.run(debug=True)
