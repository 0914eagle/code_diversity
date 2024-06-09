
class Teacher:
    def __init__(self, id):
        self.id = id
        self.class_id = id

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return str(self.id)


class Classroom:
    def __init__(self, id):
        self.id = id
        self.teacher = Teacher(id)

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return str(self.id)


class School:
    def __init__(self, num_classes, num_weeks, num_teachers):
        self.num_classes = num_classes
        self.num_weeks = num_weeks
        self.num_teachers = num_teachers
        self.classes = [Classroom(i) for i in range(1, num_classes + 1)]
        self.teachers = [Teacher(i) for i in range(1, num_teachers + 1)]
        self.weeks = []
        for i in range(num_weeks):
            self.weeks.append([])

    def add_plan(self, week, teachers):
        for teacher in teachers:
            teacher.class_id = (teacher.class_id + 1) % self.num_classes

    def get_teacher_class(self, teacher_id, week):
        return self.classes[self.teachers[teacher_id].class_id].id

    def get_class_teacher(self, class_id, week):
        return self.teachers[self.classes[class_id].teacher.id].id

    def get_class_teacher_on_tuesday(self, class_id, week):
        return self.teachers[(self.classes[class_id].teacher.id + 1) % self.num_teachers].id


def main():
    num_classes, num_weeks, num_teachers = map(int, input().split())
    school = School(num_classes, num_weeks, num_teachers)

    for _ in range(int(input())):
        query = input().split()
        if query[0] == "0":
            school.add_plan(int(query[2]), query[3:])
        else:
            teacher_id = int(query[1])
            week = int(query[2])
            class_id = school.get_teacher_class(teacher_id, week)
            print(class_id)


if __name__ == "__main__":
    main()

