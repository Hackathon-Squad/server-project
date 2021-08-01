import json


def generateAllSchedules(classes):
    classData = getClassData()
    for className in classes:
        data = classData[className]
    return "works"


def getClassData():
    file = open(
        "api/fakeClassData.json",
        "r",
    )
    return json.load(file)
