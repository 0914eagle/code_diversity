
def get_course_difficulty(course_name):
    # This function takes a course name as input and returns its difficulty
    difficulty_map = {
        "linearalgebra": 10,
        "calculus1": 10,
        "calculus2": 20,
        "honorsanalysis1": 50,
        "honorsanalysis2": 100
    }
    return difficulty_map[course_name]

def get_possible_course_schedule(course_names, k):
    # This function takes a list of course names and an integer k as input, and returns a list of possible course schedules
    possible_schedules = []
    for i in range(len(course_names)):
        course_name = course_names[i]
        if course_name.endswith("1"):
            # If the course is a Level I course, add it to the schedule
            possible_schedules.append([course_name])
        elif course_name.endswith("2"):
            # If the course is a Level II course, add it to the schedule only if the corresponding Level I course is already in the schedule
            level_i_course_name = course_name[:-1] + "1"
            for schedule in possible_schedules:
                if level_i_course_name in schedule:
                    schedule.append(course_name)
                    break
    return possible_schedules[:k]

def get_min_difficulty_sum(possible_schedules):
    # This function takes a list of possible course schedules as input and returns the minimum sum of difficulties of the courses in the schedules
    min_difficulty_sum = float("inf")
    for schedule in possible_schedules:
        difficulty_sum = 0
        for course_name in schedule:
            difficulty_sum += get_course_difficulty(course_name)
        if difficulty_sum < min_difficulty_sum:
            min_difficulty_sum = difficulty_sum
    return min_difficulty_sum

if __name__ == '__main__':
    n, k = map(int, input().split())
    course_names = []
    for i in range(n):
        course_name = input()
        course_names.append(course_name)
    possible_schedules = get_possible_course_schedule(course_names, k)
    min_difficulty_sum = get_min_difficulty_sum(possible_schedules)
    print(min_difficulty_sum)

