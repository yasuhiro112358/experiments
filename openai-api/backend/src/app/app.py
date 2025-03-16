from flask import Flask
from config import Config
from controllers.chat_controller import chat_bp

def create_app() -> Flask:
    Config.init()

    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['JSON_AS_ASCII'] = False

    app.register_blueprint(chat_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
