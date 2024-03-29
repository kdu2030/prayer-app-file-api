from flask import Flask
from flask_restx import Api
from file_manager import file_upload_namespace
from socket import gethostname

app = Flask(__name__)
api = Api(app, version="1.0", title="Prayer App File Upload API")
is_prod = 'liveconsole' in gethostname()

api.add_namespace(file_upload_namespace)


def main():
    if not is_prod:
        app.run(debug=True)


if __name__ == "__main__":
    main()
