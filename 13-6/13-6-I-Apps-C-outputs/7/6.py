
def get_courses(n, k):
    courses = []
    for i in range(n):
        name, difficulty = input().split()
        courses.append((name, int(difficulty)))
    return courses[:k]

def get_min_difficulty(courses):
    difficulty = 0
    for course in courses:
        difficulty += course[1]
    return difficulty

def solve(n, k):
    courses = get_courses(n, k)
    return get_min_difficulty(courses)

if __name__ == '__main__':
    n, k = map(int, input().split())
    print(solve(n, k))

