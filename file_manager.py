from flask_restx import Resource, Namespace
from werkzeug.datastructures import FileStorage
from typing import List, Dict
import os

file_upload_namespace = Namespace(
    "file", description="Operations for Managing Files")
file_parser = file_upload_namespace.parser()
file_parser.add_argument("file", location="files",
                         type=FileStorage, required=True)


@file_upload_namespace.route("/upload")
class FileUploadController(Resource):
    @file_upload_namespace.expect(file_parser)
    @file_upload_namespace.doc(consumes=["multipart/form-data"])
    def post(self):
        args = file_parser.parse_args()
        file: FileStorage = args["file"]

        file_path = os.path.join("./static", file.filename)
        file.save(file_path)

        return {"test": "test"}
