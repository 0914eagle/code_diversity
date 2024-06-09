
class Classroom:
    def __init__(self, number):
        self.number = number
        self.teacher = None

class Teacher:
    def __init__(self, number):
        self.number = number
        self.classroom = None

class School:
    def __init__(self, number_of_classes, number_of_teachers):
        self.number_of_classes = number_of_classes
        self.number_of_teachers = number_of_teachers
        self.classrooms = [Classroom(i) for i in range(1, number_of_classes+1)]
        self.teachers = [Teacher(i) for i in range(1, number_of_teachers+1)]

    def add_plan(self, plan):
        # Add the plan to the school
        pass

    def ask_question(self, question):
        # Ask the question and return the answer
        pass

# Test case 1
school = School(3, 3)
school.add_plan([0, 2, 2, 3, 2])
school.add_plan([0, 3, 1, 2, 1])
school.add_plan([0, 1, 1, 2, 3])
print(school.ask_question([1, 3, 2]))
print(school.ask_question([1, 2, 4]))
print(school.ask_question([1, 1, 4]))

# Test case 2
school = School(3, 3)
school.add_plan([0, 2, 2, 3, 2])
school.add_plan([0, 3, 1, 2, 1])
school.add_plan([0, 1, 1, 2, 3])
print(school.ask_question([1, 3, 2]))
print(school.ask_question([1, 2, 4]))
print(school.ask_question([1, 1, 4]))

