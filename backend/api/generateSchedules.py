import json


def generateAllSchedules(classes):
    classData = getClassData()
    courseList = classData["courseList"]
    classesSet = set(classes)
    classesInfo = {}
    for course in courseList:
        className = (
            course["subjectCode"].replace(" ", "")
            + " "
            + course["courseCode"].replace(" ", "")
        )
        if className in classesSet:
            classesInfo.update(
                {
                    className: {
                        "lectures": [],
                        "sections": [],
                    }
                }
            )
            for i in range(len(course["sections"])):
                sectionCode = course["sections"][i]["sectionCode"]
                sectionTimes = course["sections"][i]["recurringMeetings"]
                if sectionCode[1:] != "00":
                    classesInfo[className]["sections"].append(
                        {sectionCode: sectionTimes}
                    )
                else:
                    classesInfo[className]["lectures"].append(
                        {sectionCode: sectionTimes}
                    )
    return classesInfo


def getClassData():
    file = open(
        "api/classData.json",
        "r",
    )
    return json.load(file)
