from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user_name：passed@localhost:5432/your_db'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app=app)


class students(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    # Id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    name = db.Column('name', db.String(100))
    city = db.Column('city', db.String(50))
    addr = db.Column('addr', db.String(200))
    pin = db.Column('pin', db.String(10))


def __init__(self, name, city, addr, pin):
    self.name = name
    self.city = city
    self.addr = addr
    self.pin = pin


@app.route('/')
def show_all():
    return render_template('./show_all.html', students=students.query.all())


@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['city'] or not request.form['addr']:
            flash('Please enter all the fields', 'error')
        else:
            # student = students(name=request.form['name'], city=request.form['city'],
            #                    addr=request.form['addr'], pin=request.form['pin'])
            student = students()
            student.name = request.form['name']
            student.city = request.form['city']
            student.addr = request.form['addr']
            student.pin = request.form['pin']

            db.session.add(student)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('show_all'))
    return render_template('./new.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
