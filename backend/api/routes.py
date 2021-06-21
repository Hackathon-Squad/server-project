from flask import Blueprint
from pymongo import MongoClient
import os

api = Blueprint("api", __name__, url_prefix="/api")


@api.route("/testDBConnection")
def connectToDB():
    connectionString = os.getenv("MONGO_URI")
    client = MongoClient(connectionString)
    db = client["projectDB"]
    data = db["data"]
    currentData = data.find()

    for item in currentData:
        return item["test"]
