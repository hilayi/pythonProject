from DB.python_mongo_db import PyMongoDB


class MainController:
    @staticmethod
    def get_db():
        return PyMongoDB.get_db()

    @staticmethod
    def get_app():
        return PyMongoDB.get_app()





