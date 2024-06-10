
import sys
import itertools

def get_input():
    n, k = map(int, input().split())
    courses = []
    for i in range(n):
        name, difficulty = input().split()
        courses.append((name, int(difficulty)))
    return n, k, courses

def get_prerequisites(courses):
    prerequisites = {}
    for course in courses:
        if '1' in course[0]:
            prerequisites[course[0]] = course[0].replace('1', '2')
    return prerequisites

def get_courses_by_level(courses, prerequisites):
    courses_by_level = {}
    for course in courses:
        level = 1
        if course[0] in prerequisites:
            level = 2
        if course[0] not in courses_by_level:
            courses_by_level[level] = []
        courses_by_level[level].append(course)
    return courses_by_level

def get_possible_course_combinations(courses_by_level, k):
    possible_combinations = []
    for level in range(1, 3):
        if level in courses_by_level:
            possible_combinations.extend(itertools.combinations(courses_by_level[level], k))
    return possible_combinations

def get_min_difficulty(courses, prerequisites, possible_combinations):
    min_difficulty = sys.maxsize
    for combination in possible_combinations:
        difficulty = 0
        for course in combination:
            difficulty += course[1]
            if course[0] in prerequisites and prerequisites[course[0]] not in combination:
                difficulty += 1
        if difficulty < min_difficulty:
            min_difficulty = difficulty
    return min_difficulty

def main():
    n, k, courses = get_input()
    prerequisites = get_prerequisites(courses)
    courses_by_level = get_courses_by_level(courses, prerequisites)
    possible_combinations = get_possible_course_combinations(courses_by_level, k)
    print(get_min_difficulty(courses, prerequisites, possible_combinations))

if __name__ == '__main__':
    main()

