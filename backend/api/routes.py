from flask import Blueprint
from flask import request
from pymongo import MongoClient
import os
from .generateSchedules import generateAllSchedules

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


@api.route("/generateSchedules", methods=["POST"])
def generateSchedules():
    classes = request.get_json()["classes"]
    generateAllSchedules(classes)
    return "works"
