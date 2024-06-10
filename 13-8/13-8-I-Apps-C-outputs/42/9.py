
import sys
import itertools

def get_input():
    n, k = map(int, input().split())
    courses = []
    for i in range(n):
        name, diff = input().split()
        courses.append((name, int(diff)))
    return n, k, courses

def get_courses(courses, k):
    courses.sort(key=lambda x: x[1])
    return courses[:k]

def get_difficulty(courses):
    return sum(course[1] for course in courses)

def main():
    n, k, courses = get_input()
    courses = get_courses(courses, k)
    print(get_difficulty(courses))

if __name__ == '__main__':
    main()

