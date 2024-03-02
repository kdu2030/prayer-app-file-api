from flask import Blueprint
from flask_restx import Resource, Namespace

test_api = Namespace("test", description="Test operations")


@test_api.route("/test")
class Test(Resource):
    def get(self):
        return {"hello": "world"}
