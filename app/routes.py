from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, ShopEdit
from app.models import Shop
from app.models import Shop_donut
from app.models import Donut
from app.models import User

@app.route('/shops', methods= ['GET'])
def shops():
  shops= Shop.query.all()
  return render_template('shops.html', shops=shops)

@app.route('/shops/<id>')
def shop_profile(id):
  shop_data = Shop.query.filter_by(id=id).first_or_404()
  shop_donut = Shop_donut.query.filter_by(shop_id=id).first_or_404()
  donut = Donut.query.filter_by(id = shop_donut.donut_id).first_or_404()
  employee = User.query.filter_by(shop_id = id).first_or_404()
  shop = {
    'id': shop_data.id,
    'shop_name': shop_data.name,
    'shop_city': shop_data.city,
    'donut': donut.name,
    'employee': {'first_name': employee.first_name, 'last_name': employee.last_name}
  }
  return render_template('shop_profile.html', shop=shop)
  
@app.route('/shops/edit/<id>', methods=['GET','POST'])
def shop_edit(id):
  shop= Shop.query.filter_by(id=id).first_or_404()
  return render_template('shop_edit.html', shop=shop)

@app.route('/shops/edit/update', methods=['POST'])
def update_shop():
  shop_id = request.form.get('shop_id')
  newname = request.form.get('shop_name')
  newcity = request.form.get('shop_city')
  shop = Shop.query.filter_by(id=shop_id).first()
  shop.name = newname
  shop.city = newcity
  db.session.commit()
  return redirect(f'/shops/{shop_id}')

@app.route('/shops/delete/<id>')
def shop_confirm_delete(id):
  shop= Shop.query.filter_by(id=id).first_or_404()
  return render_template('confirm_delete.html', shop=shop)

@app.route('/shops/delete/confirm', methods=['POST'])
def shop_delete():
  shop_id = request.form.get('shop_id')
  shop = Shop.query.filter_by(id=shop_id).first()
  db.session.delete(shop)
  db.session.commit()
  return redirect('/shops')
  

@app.route('/shops/new')
def new_shop():
  return render_template('shop_new.html')

@app.route('/shops/add', methods=['POST'])
def add_shop():
  name = request.form.get('shop_name')
  city = request.form.get('shop_city')
  new_shop = Shop(name=name, city=city)
  db.session.add(new_shop)
  db.session.commit()
  return redirect('/shops')

@app.route('/login', methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
    return redirect(url_for('index'))
  return render_template('login.html', title='Sign In', form=form)


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
  # NOTES:
  # The two strange @app.route lines above the function are decorators
  # A decorator modifies the function that follows it. A common pattern 
  # with decorators is to use them to register functions as callbacks 
  # for certain events.