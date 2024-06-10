
def get_course_difficulty(course_name):
    # This function takes a course name as input and returns its difficulty
    # You can write your own code to retrieve the difficulty of a course based on its name
    # For example, you can use a dictionary to map course names to difficulties
    return difficulty

def get_min_difficulty_courses(courses, k):
    # This function takes a list of courses and an integer k as input and returns the minimum sum of difficulties of the k courses
    # You can use a sorting algorithm, such as selection sort or insertion sort, to find the k courses with the minimum sum of difficulties
    return courses

def main():
    n, k = map(int, input().split())
    courses = []
    for i in range(n):
        course_name, difficulty = input().split()
        courses.append((course_name, int(difficulty)))
    courses = sorted(courses, key=lambda x: x[1])
    min_difficulty_courses = get_min_difficulty_courses(courses, k)
    total_difficulty = sum(course[1] for course in min_difficulty_courses)
    print(total_difficulty)

if __name__ == '__main__':
    main()

