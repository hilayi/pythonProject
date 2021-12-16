from pymongo import MongoClient
from flask import Flask


class PyMongoDB:
    @staticmethod
    def get_db():
        client = MongoClient('localhost', 27017)
        return client['HilaDB']

    @staticmethod
    def get_app():
        return Flask(__name__)

