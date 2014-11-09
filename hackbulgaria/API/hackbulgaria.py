import json
import requests
from student import Student
from course import Course


class Hackbulgaria():
	def __init__(self):
		self.students = []
		self.course_one = set()
		self.course_two = set()


	def getStudents(self, link):
		r = requests.get(link, verify=False)
		students = r.json()
		status = r.status_code
		r.encoding
		if status == 200:
			for student in students:
				github = student['github']
				names = student['name']
				courses = student['courses']
				available = student['available']
				one = Student(names, github, courses, available)
				self.students.append(one)
		else:
			return 0;

	def getCourses(self):
		for student in self.students:
			studentCourses = student.courses
			for studentCourse in studentCourses:
				one = Course(studentCourse['name'],studentCourse['group'])
				if studentCourse['group'] == 1:
					self.course_one.add(studentCourse['name'])
				if studentCourse['group'] == 2:
					self.course_two.add(studentCourse['name'])
					
	def print_grups(self):
		print("Group: 1")
		i = 0
		for one in self.course_one:
			print("[" + str(i) + "] " + one)
			i = i + 1
		print("Group: 2")
		i = 0
		for one in self.course_two:
			print("[" + str(i) + "] " + one)
			i = i + 1
	




def main():
	hack = Hackbulgaria()
	hack.getStudents('https://hackbulgaria.com/api/students/')
	hack.getCourses()
	hack.print_grups()

if __name__ == '__main__':
	main()