
import sys
import math

def get_course_info(n, k):
    course_info = []
    for i in range(n):
        line = sys.stdin.readline().strip()
        name, difficulty = line.split()
        course_info.append((name, int(difficulty)))
    return course_info

def get_level_courses(course_info):
    level_courses = []
    for name, difficulty in course_info:
        if name[-1] == '1':
            level_courses.append((name, difficulty))
    return level_courses

def get_prerequisite_courses(course_info, level_courses):
    prerequisite_courses = []
    for name, difficulty in course_info:
        if name[-1] == '2':
            prerequisite_courses.append((name, difficulty))
    return prerequisite_courses

def get_course_schedule(course_info, level_courses, prerequisite_courses):
    course_schedule = []
    for name, difficulty in course_info:
        if name in level_courses:
            course_schedule.append((name, difficulty))
        elif name in prerequisite_courses:
            course_schedule.append((name, difficulty))
    return course_schedule

def get_min_difficulty_sum(course_schedule):
    return sum(difficulty for name, difficulty in course_schedule)

if __name__ == '__main__':
    n, k = map(int, input().split())
    course_info = get_course_info(n, k)
    level_courses = get_level_courses(course_info)
    prerequisite_courses = get_prerequisite_courses(course_info, level_courses)
    course_schedule = get_course_schedule(course_info, level_courses, prerequisite_courses)
    print(get_min_difficulty_sum(course_schedule))

