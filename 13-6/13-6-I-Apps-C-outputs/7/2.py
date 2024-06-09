
def get_courses(n, k):
    courses = []
    for i in range(n):
        name, difficulty = input().split()
        courses.append((name, int(difficulty)))
    return courses[:k]

def get_min_difficulty(courses):
    difficulty = 0
    for course, d in courses:
        difficulty += d
    return difficulty

def get_schedule(courses):
    schedule = []
    for course, d in sorted(courses, key=lambda x: x[1], reverse=True):
        schedule.append(course)
    return schedule

def main():
    n, k = map(int, input().split())
    courses = get_courses(n, k)
    difficulty = get_min_difficulty(courses)
    schedule = get_schedule(courses)
    print(difficulty)
    for course in schedule:
        print(course)

if __name__ == '__main__':
    main()

