
def reassign_teachers(teachers, weeks, plans):
    # Initialize a dictionary to store the classroom assignments for each teacher and week
    assignments = {}
    for teacher in teachers:
        assignments[teacher] = {}
        for week in weeks:
            assignments[teacher][week] = teacher

    # Iterate through the plans and update the assignments accordingly
    for plan in plans:
        teacher, week, classes = plan
        current_class = assignments[teacher][week]
        for i in range(classes):
            next_class = (current_class + 1) % len(teachers)
            assignments[teacher][week] = next_class
            current_class = next_class

    return assignments

def get_class(assignments, teacher, week):
    return assignments[teacher][week]

def main():
    N, M, Q = map(int, input().split())
    teachers = list(range(1, N + 1))
    weeks = list(range(1, M + 1))
    plans = []
    for i in range(Q):
        query = input().split()
        if query[0] == "0":
            plans.append((int(query[1]), int(query[2]), int(query[3:])))
        else:
            teacher, week = map(int, query[1:])
            print(get_class(reassign_teachers(teachers, weeks, plans), teacher, week))

if __name__ == '__main__':
    main()

