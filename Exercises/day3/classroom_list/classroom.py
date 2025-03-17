# #get input from the user
# firstname = input("Enter your firstname: ")
# lastname = input("Enter your lastname: ")
# subjectArea = input("Enter your subject area: ")
# course = input("Enter the name of the course you teach: ")

#define the Person class
class Person():

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    
    def printname(self):
        fullname = self.firstname +' '+ self.lastname
        return fullname

#define the Student class
class Student(Person):
    def __init__(self, firstname, lastname, subjectArea): 
        Person.__init__(self, firstname, lastname)
        self.subjectArea = subjectArea
    
    def printNameSubject(self):
        fullnameSubject = 'Full name: ' + self.firstname + " " + self.lastname + ". Subject area: " + self.subjectArea
        print(fullnameSubject)

#define the Teacher class
class Teacher(Person):
    def __init__(self, firstname, lastname, course):
        Person.__init__(self, firstname, lastname)
        self.course = course
    
    def printNameCourse(self):
        fullnameCourse = 'Full name: ' + self.firstname + " " + self.lastname + ". Course name: " + self.course
        print(fullnameCourse)


    
# #create an instance of the Person class
# person = Person(firstname, lastname)

# student = Student(firstname, lastname, subjectArea)

# #display the full name
# print("The full name is :", student.printNameSubject())

    
    



