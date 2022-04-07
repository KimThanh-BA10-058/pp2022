# init data
studentList = list()
courseList = list()
markList = list()


# add student function 

def addStudent():
    numberOfStudent = int(input("Number of student: "))
    print("Input student info: ")
    for i in range(numberOfStudent):
        print("Student", i + 1)
        student = {
            "id": input("id: "),
            "name": input("name: "),
            "DoB": input("DoB: ")
        }
        studentList.append(student)


# print student list

def printListStudent():
    numberOfStudent = len(studentList)
    print("\nThere are", numberOfStudent, "students in the class")
    for i in range(numberOfStudent):
        print("Student", i + 1, ":", studentList[i])


def getStudentInfo(studentId):
    for student in studentList:
        if studentId == student.get("id"):
            return student


# add course

def addCourse():
    numCourse = int(input("How many courses are there in the semester ?"))
    for i in range(numCourse):
        course = {
            "id": input("id: "),
            "name": input("name: ")
        }
        courseList.append(course)


def printListCourse():
    print("There are %s courses in the semester" % len(courseList))
    for course in courseList:
        print("course info: ", course)


def getSelectCourse():
    for i in range(len(courseList)):
        print("Enter", i, "for", courseList[i].get("name"))
    courseIndex = int(input("Your selection: "))
    if courseIndex > len(courseList) or courseIndex < 0:
        return {}
    else:
        return courseList[courseIndex]
        # add mark for each student


def addMark():
    for course in courseList:
        print("Enter mark for course ", course.get("name"))
        for student in studentList:
            studentName = student.get("name")
            mark = {
                "courseId": course.get("id"),
                "studentId": student.get("id"),
                "value": int(input(f"Mark for {studentName}: "))
            }
            markList.append(mark)


def printAllMarksForSelectedCourse():
    selectedCourse = getSelectCourse()
    if selectedCourse:
        for mark in markList:
            if mark.get("courseId") == selectedCourse.get("id"):
                studentInfo = getStudentInfo(mark.get("studentId"))
                print("Mark for student", studentInfo.get("name"), "in course: ", mark.get("value"))
    else:
        print("No course info")


addStudent()
printListStudent()

addCourse()
printListCourse()

addMark()
printAllMarksForSelectedCourse()
