from flask import Flask
from app.routes import main_bp
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Register Blueprints
app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(debug=True)
