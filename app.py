from flask import Flask
from config import Config
from models import db
from routes import auth_bp, blog_bp
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

from models import User
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(blog_bp)  # home at '/'

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
