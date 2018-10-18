from app import app, db
from app.models import Shop, Donut, Shop_donut, User

@app.shell_context_processor
def make_shell_context():
  return {'db':db, 'Shop':Shop, 'Donut':Donut, 'Shop_donut':Shop_donut, 'User':User}