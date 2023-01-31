"""
This is a game of guessing number within 1-100.
"""
import random
from flask import Flask, render_template, flash, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Guess Number simple version'
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
bootstrap = Bootstrap(app)


class InputForm(FlaskForm):
    number = IntegerField('Please enter an integer (1~100)', validators=[
        # DataRequired('Invalid input!'),
        # NumberRange(1, 100, 'Please enter an integer within 1-100!')])
        DataRequired(),
        NumberRange(1, 100)])
    submit = SubmitField('submit')


@app.route('/')
def index():
    # generate a random integer within 1-100 and store it
    session['number'] = random.randint(1, 100)
    # The number of guesses is initialized to 10
    session['times'] = 10
    return render_template('index.html')


@app.route('/guess', methods=['GET', 'POST'])
def guess():
    times = session['times']
    true_value = session['number']
    form = InputForm()
    if form.validate_on_submit():
        times -= 1
        session['times'] = times
        guess_value = form.number.data

        # lose
        if times < 0 or (times == 0 and guess_value != true_value):
            flash('You Lose! T_T~~', 'danger')
            return redirect(url_for('index'))
        # continue
        if guess_value > true_value:
            flash('Too large！You only have %s more chances.' % times, 'warning')
        elif guess_value < true_value:
            flash('Too small！You only have %s more chances.' % times, 'warning')
        else:
            flash('You win! ^_^~~', 'success')
            return redirect(url_for('index'))
        return redirect(url_for('guess'))
    return render_template('guess.html', form=form)


if __name__ == '__main__':
    app.run(port=5000, debug=True)