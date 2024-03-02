from flask import Flask
from flask_restx import Api
from file_manager import file_upload_namespace
from socket import gethostname
from constants import LOCAL_API_URL, PRODUCTION_API_URL

app = Flask(__name__)
api = Api(app, version="1.0", title="Prayer App File Upload API")
is_prod = 'liveconsole' in gethostname()
app.config["APP_URL"] = PRODUCTION_API_URL if is_prod else LOCAL_API_URL

api.add_namespace(file_upload_namespace)


def main():
    if not is_prod:
        app.run(debug=True)


if __name__ == "__main__":
    main()
