from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField
from wtforms.validators import DataRequired, InputRequired

app = Flask(__name__)

app.secret_key = "i_am_secret"

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField("Login")

@app.route("/")
def home():
    form = LoginForm()
    return render_template('index.html', form=form)

@app.route("/login", methods=["GET","POST"])
def login():
    login_form = LoginForm()
    login_form.validate_on_submit()
    return render_template('index.html', form=login_form)

if __name__ == '__main__':
    app.run(debug=True)
