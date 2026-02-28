from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm
from models import db,User

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret!123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = RegistrationForm()
    if form.validate_on_submit():

        user = User(username= form.username.data, email= form.email.data, password= form.password.data)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('success'))
    return render_template('index.html', form=form)

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)

