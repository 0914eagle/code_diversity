
def rotate_teachers(teachers, week, plan):
    # Rotate the teachers according to the plan
    for i in range(len(plan)):
        teachers[plan[i] - 1] = teachers[plan[i] - 1] + 1
        if teachers[plan[i] - 1] > week:
            teachers[plan[i] - 1] = 1
    return teachers

def query(teachers, week, query):
    # Query the class where teacher 'd' teaches on Tuesday of the 'x'-th week
    if query[0] == 0:
        # Add a plan to rotate the teachers
        rotate_teachers(teachers, week, query[1:])
    else:
        # Query the class where teacher 'd' teaches on Tuesday of the 'x'-th week
        return teachers[query[1] - 1]

def main():
    N, M, Q = map(int, input().split())
    teachers = [i for i in range(1, N + 1)]
    week = 0
    plans = []
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 0:
            # Add a plan to rotate the teachers
            plans.append(query[1:])
        else:
            # Query the class where teacher 'd' teaches on Tuesday of the 'x'-th week
            print(query(teachers, week, query))

if __name__ == '__main__':
    main()

