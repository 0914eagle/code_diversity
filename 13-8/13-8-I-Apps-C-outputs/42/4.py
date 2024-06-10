
import sys
import math

def get_input():
    n, k = map(int, input().split())
    courses = []
    for i in range(n):
        name, diff = input().split()
        courses.append((name, int(diff)))
    return n, k, courses

def is_level_i(name):
    return name[-1].isdigit() and int(name[-1]) == 1

def is_level_ii(name):
    return name[-1].isdigit() and int(name[-1]) == 2

def get_level_i_courses(courses):
    return [course for course in courses if is_level_i(course[0])]

def get_level_ii_courses(courses):
    return [course for course in courses if is_level_ii(course[0])]

def get_level_i_course_names(courses):
    return [course[0] for course in courses if is_level_i(course[0])]

def get_level_ii_course_names(courses):
    return [course[0] for course in courses if is_level_ii(course[0])]

def get_course_difficulties(courses, names):
    return [course[1] for course in courses if course[0] in names]

def get_min_difficulty_sum(courses, k):
    level_i_courses = get_level_i_courses(courses)
    level_ii_courses = get_level_ii_courses(courses)
    level_i_course_names = get_level_i_course_names(courses)
    level_ii_course_names = get_level_ii_course_names(courses)
    level_i_difficulties = get_course_difficulties(level_i_courses, level_i_course_names)
    level_ii_difficulties = get_course_difficulties(level_ii_courses, level_ii_course_names)
    level_i_course_sum = sum(level_i_difficulties)
    level_ii_course_sum = sum(level_ii_difficulties)
    min_difficulty_sum = math.inf
    for i in range(1, k+1):
        min_difficulty_sum = min(min_difficulty_sum, level_i_course_sum + level_ii_course_sum - i*level_i_difficulties[0])
    return min_difficulty_sum

def main():
    n, k, courses = get_input()
    print(get_min_difficulty_sum(courses, k))

if __name__ == '__main__':
    main()

