
import sys
import itertools

def get_input():
    n, k = map(int, input().split())
    courses = []
    for i in range(n):
        course, difficulty = input().split()
        courses.append((course, int(difficulty)))
    return n, k, courses

def get_courses_per_semester(courses, k):
    courses_per_semester = []
    for i in range(2):
        courses_per_semester.append([])
    for course, difficulty in courses:
        if course.endswith("1"):
            courses_per_semester[0].append((course, difficulty))
        elif course.endswith("2"):
            courses_per_semester[1].append((course, difficulty))
        else:
            courses_per_semester[0].append((course, difficulty))
    return courses_per_semester

def get_min_difficulty(courses_per_semester):
    min_difficulty = 0
    for semester in courses_per_semester:
        min_difficulty += min(course[1] for course in semester)
    return min_difficulty

def get_min_difficulty_with_constraints(courses_per_semester):
    min_difficulty = 0
    for semester in courses_per_semester:
        courses = sorted(semester, key=lambda x: x[1])
        min_difficulty += courses[0][1]
    return min_difficulty

def main():
    n, k, courses = get_input()
    courses_per_semester = get_courses_per_semester(courses, k)
    min_difficulty = get_min_difficulty_with_constraints(courses_per_semester)
    print(min_difficulty)

if __name__ == '__main__':
    main()

