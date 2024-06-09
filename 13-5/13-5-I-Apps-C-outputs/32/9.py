
def get_bug_complexity(bug_complexities):
    return sorted(bug_complexities, reverse=True)

def get_student_abilities(student_abilities):
    return sorted(student_abilities, reverse=True)

def get_passes_needed(student_passes):
    return sum(student_passes)

def get_optimal_schedule(bug_complexities, student_abilities, student_passes, passes_needed):
    bug_complexity = get_bug_complexity(bug_complexities)
    student_ability = get_student_abilities(student_abilities)
    passes_needed = get_passes_needed(student_passes)

    schedule = []
    for i in range(len(bug_complexity)):
        for j in range(len(student_ability)):
            if student_ability[j] >= bug_complexity[i] and passes_needed > 0:
                schedule.append(j + 1)
                passes_needed -= 1
                break
        if passes_needed == 0:
            break

    return schedule

def main():
    n, m, s = map(int, input().split())
    bug_complexities = list(map(int, input().split()))
    student_abilities = list(map(int, input().split()))
    student_passes = list(map(int, input().split()))

    schedule = get_optimal_schedule(bug_complexities, student_abilities, student_passes, s)

    if len(schedule) == m:
        print("YES")
        print(" ".join(map(str, schedule)))
    else:
        print("NO")

if __name__ == '__main__':
    main()

