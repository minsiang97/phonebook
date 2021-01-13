import os
import config
from flask import Flask
from models.base_model import db
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.peewee import ModelView
from models.user import User
from flask_wtf.csrf import CSRFProtect

web_dir = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'phonebook_web')

app = Flask('PhoneBook', root_path=web_dir)
admin = Admin(app)

admin.add_view(ModelView(User))

csrf = CSRFProtect(app)

if os.getenv('FLASK_ENV') == 'production':
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")


@app.before_request
def before_request():
    db.connect()


@app.teardown_request
def _db_close(exc):
    if not db.is_closed():
        print(db)
        print(db.close())
    return exc
