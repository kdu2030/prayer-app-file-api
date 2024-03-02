from flask_restx import Resource, Namespace
from werkzeug.datastructures import FileStorage
from typing import List, Dict
import os
import random
import string
from constants import FILE_NAME_STRING_LENGTH
from flask import current_app

file_upload_namespace = Namespace(
    "file", description="Operations for Managing Files")
file_parser = file_upload_namespace.parser()
file_parser.add_argument("file", location="files",
                         type=FileStorage, required=True)


@file_upload_namespace.route("/upload")
class FileManagerController(Resource):
    @file_upload_namespace.expect(file_parser)
    @file_upload_namespace.doc(consumes=["multipart/form-data"])
    def post(self):
        args = file_parser.parse_args()
        file: FileStorage = args["file"]

        file_ext = file.filename.split(".")[-1]
        random_file_name = "".join(random.choices(
            string.ascii_lowercase + string.digits, k=FILE_NAME_STRING_LENGTH))
        complete_file_name = f"{random_file_name}.{file_ext}"

        file_path = os.path.join("./static", complete_file_name)
        file.save(file_path)

        app_url = current_app.config.get("APP_URL")

        return {"fileUrl": f"{app_url}/static/{complete_file_name}"}
