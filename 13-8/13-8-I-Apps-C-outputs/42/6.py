
import sys
import itertools

def get_input():
    n, k = map(int, input().split())
    courses = []
    for _ in range(n):
        course, diff = input().split()
        courses.append((course, int(diff)))
    return n, k, courses

def get_levels(courses):
    levels = []
    for course, _ in courses:
        if course[-1].isdigit():
            levels.append(course[-1])
    return levels

def get_prereqs(courses):
    prereqs = []
    for course, _ in courses:
        if course[-1].isdigit():
            prereqs.append(course[:-1])
    return prereqs

def get_difficulty(courses, prereqs, levels, k):
    difficulty = 0
    for course, diff in courses:
        if course in prereqs:
            continue
        if course[-1].isdigit():
            if course[:-1] in levels:
                difficulty += diff
        else:
            difficulty += diff
    return difficulty

def solve(n, k, courses):
    levels = get_levels(courses)
    prereqs = get_prereqs(courses)
    difficulty = get_difficulty(courses, prereqs, levels, k)
    return difficulty

if __name__ == '__main__':
    n, k, courses = get_input()
    print(solve(n, k, courses))

