
def get_bug_complexity(bug_complexities):
    return bug_complexities

def get_student_ability(student_abilities):
    return student_abilities

def get_student_passes(student_passes):
    return student_passes

def can_fix_bug(student_ability, bug_complexity):
    return student_ability >= bug_complexity

def get_optimal_solution(student_abilities, bug_complexities, student_passes, max_passes):
    students_to_fix_bugs = []
    days_to_fix_bugs = 0
    passes_given = 0

    for bug_complexity in sorted(bug_complexities, reverse=True):
        for student_ability in sorted(student_abilities, reverse=True):
            if can_fix_bug(student_ability, bug_complexity):
                students_to_fix_bugs.append(student_ability)
                days_to_fix_bugs += 1
                passes_given += student_passes[student_ability]
                break

    if passes_given > max_passes:
        return "NO"

    return "YES\n" + " ".join(map(str, students_to_fix_bugs))

if __name__ == '__main__':
    student_abilities = [2, 3, 1, 2]
    bug_complexities = [1, 3, 1, 2]
    student_passes = [3, 6, 1, 3]
    max_passes = 9
    print(get_optimal_solution(student_abilities, bug_complexities, student_passes, max_passes))

