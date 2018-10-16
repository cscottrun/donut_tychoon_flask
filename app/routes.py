from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
  shop = {'shop_name': "Carrie's Donuts"}
  donuts = [
    {
      'donut_name': 'chocolate',
      'price': '3.50'
    },
    {
      'donut_name': 'glazed',
      'price': '2.50'
    }
  ]
  return render_template('index.html', title='Home', shop = shop, donuts = donuts)

@app.route('/login', methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
    return redirect(url_for('index'))
  return render_template('login.html', title='Sign In', form=form)

  # NOTES:
  # The two strange @app.route lines above the function are decorators
  # A decorator modifies the function that follows it. A common pattern 
  # with decorators is to use them to register functions as callbacks 
  # for certain events.