from pymongo import MongoClient
from flask import Flask

app = Flask(__name__)
import Routes.skill_routes
import Routes.candidate_routes
import Routes.job_routes

client = MongoClient('localhost', 27017)
db = client['HilaDB']


def main():
    print("Hi")


if __name__ == "__main__":
    app.run()
