
import sys
input = sys.stdin.read()
n, k = map(int, input.split('\n')[0].split())
courses = {}
for i in range(1, n+1):
    course, difficulty = input.split('\n')[i].split()
    courses[course] = int(difficulty)

def find_min_difficulty(courses, k):
    # Initialize the minimum difficulty sum to infinity
    min_difficulty = float('inf')
    # Initialize the current difficulty sum to 0
    current_difficulty = 0
    # Initialize the number of courses taken to 0
    num_courses = 0
    # Sort the courses by difficulty in ascending order
    sorted_courses = sorted(courses.items(), key=lambda x: x[1])
    # Iterate through the sorted courses
    for course, difficulty in sorted_courses:
        # If the current difficulty sum plus the difficulty of the current course is less than or equal to the minimum difficulty sum, and the number of courses taken is less than or equal to k, update the minimum difficulty sum and the current difficulty sum
        if current_difficulty + difficulty <= min_difficulty and num_courses + 1 <= k:
            min_difficulty = current_difficulty + difficulty
            current_difficulty += difficulty
            num_courses += 1
    # Return the minimum difficulty sum
    return min_difficulty

def f1(...):
    ...
    return ...

def f2(...):
    ...
    return ...

if __name__ == '__main__':
    f1(...)
    f2(...)

