from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mrsoft'


class LoginForm(FlaskForm):
    name = StringField(label='Username', validators=[DataRequired("User name cannot be empty!")])
    password = PasswordField(label='password', validators=[DataRequired("Password cannot be empty!")])
    submit = SubmitField(label='Submit')


#@app.route('/')
#def hello_world():
#    return render_template('index.html')


#@app.route('/user/<username>')
#def show_user_profile(username):
#    return render_template('user.html', name=username)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    data = {}
    if form.validate_on_submit():
        data['name'] = form.name.data
        data['password'] = form.password.data
    return render_template('index.html', form=form, data=data)


if __name__ == '__main__':
    app.run(debug=True)
