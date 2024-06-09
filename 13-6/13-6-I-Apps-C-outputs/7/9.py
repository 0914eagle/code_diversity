
def get_course_info(n):
    course_info = {}
    for i in range(n):
        course_name, difficulty = input().split()
        course_info[course_name] = int(difficulty)
    return course_info

def get_prerequisites(course_info):
    prerequisites = {}
    for course_name, difficulty in course_info.items():
        if course_name[-1] == '1':
            prerequisites[course_name] = course_name[:-1]
    return prerequisites

def get_courses_to_take(course_info, prerequisites, k):
    courses_to_take = []
    for course_name, difficulty in sorted(course_info.items(), key=lambda x: x[1]):
        if course_name not in courses_to_take:
            if course_name in prerequisites:
                if prerequisites[course_name] in courses_to_take:
                    courses_to_take.append(course_name)
            else:
                courses_to_take.append(course_name)
            if len(courses_to_take) == k:
                break
    return courses_to_take

def get_total_difficulty(courses_to_take, course_info):
    total_difficulty = 0
    for course_name in courses_to_take:
        total_difficulty += course_info[course_name]
    return total_difficulty

def main():
    n, k = map(int, input().split())
    course_info = get_course_info(n)
    prerequisites = get_prerequisites(course_info)
    courses_to_take = get_courses_to_take(course_info, prerequisites, k)
    total_difficulty = get_total_difficulty(courses_to_take, course_info)
    print(total_difficulty)

if __name__ == '__main__':
    main()

