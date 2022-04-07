import numpy as np
import math

studentList = list()
courseList = list()
markList = list()

class Student:
    def addStudentDetails(self, id, name, Dob):
        self._name = name
        self._DoB = Dob
        self.id = id

        return self

    def addStudent(self):
        student = {
            "Student ID": self.id,
            "Student name": self._name,
            "Student DoB": self._DoB,
            "marks": {}
        }
        studentList.append(student)
        return studentList
def __str__(self):
    attrs = vars(self)
    print('', '.join("%s: %s" % item for item in attrs.items())')

def inputListOfStudents():
    numberOfStudent = int(input("Number of student: "))
    print("Input student info: ")
    for i in range(numberOfStudent):
        print("Student", i + 1)
        student = Student()
        student.addStudentDetails(input("Student ID: "), input("Student Name: "), input("Student DoB: "))
        student.addStudent()

def showListStudents():
    for student in studentList:
        print(student)
        return studentList


inputListOfStudents()
showListStudents()

class Course:
    def addCourseDetails(self, id, name):
        self._nameofcourse = name
        self.idofcourse = id
        return self

    def addCourse(self):
        course = {
            "Course ID": self.idofcourse,
            "Course name": self._nameofcourse
        }
        courseList.append(course)
        return courseList


def __str__(self):
    attrs = vars(self)
    print('', '.join("%s: %s" % item for item in attrs.items())')

def inputListOfCourses():
    numberOfCourse = int(input("Number of course: "))
    print("Input course info: ")
    for i in range(numberOfCourse):
        print("Course: ", i + 1)
        course = Course()
        course.addCourseDetails(input("Course ID: "), input("Course Name: "))
        course.addCourse()

def showListCourses():
    for course in courseList:
        print(course)
        return courseList


inputListOfCourses()
showListCourses()


class Mark:
    def selectthecourse(courseList):
        for course in courseList:
            print(course)
        course_Id = input("Enter Id of of the given course: ")
        return course_Id

    def inputMark(courseId, studentList):
        for course in courseList:
            students = studentList
            print(f"Enter mark of the course {courseId} for students")
            for student in students:
                Mark = float(input(f"- Enter the mark of student: {student['Student ID']}-{student['Student name']}: "))

                student['marks'][courseId] = Mark

    def displayMark(courseId, studentList):
        print(f"This is the mark for the course {courseId}")
        for student in studentList:
            print(f"{student['Student ID']:<5} {student['Student name']:<30} {student['marks'][courseId]:<10}")

    def MarkoftheGivenCourse(course_Id, studentList):
        Mark.inputMark(course_Id, studentList)
        Mark.displayMark(course_Id, studentList)

    def chooseCourseToAddMark(courseList, studentList):
        course_Id = Mark.selectthecourse(courseList)
        Mark.MarkoftheGivenCourse(course_Id, studentList)

Mark.chooseCourseToAddMark(courseList, studentList)

def calculate_average_GPA(studentList):
        student_ID =  input("Enter the student Id you want to caculate avg GPA: ")
        for student in studentList:
            if student_ID == student['Student ID']:
                No_of_credit = 0
                total_point = 0
                course_ID = list(student['marks'].keys())
                value = list(student['marks'].values())
                arrayPoints = np.array(value)
                for i in range(len(arrayPoints)):
                    print(f"This is the point of the course {course_ID[i]}: {arrayPoints[i]}")
                    credit = int(input(f"Enter number of credits you want of the course for the students {student['Student ID']}: "))
                    No_of_credit += credit
                    points = arrayPoints[i] * credit
                    total_point += points
                GPA = float(total_point) / No_of_credit
            return GPA
        print(GPA)
calculate_average_GPA(studentList)
