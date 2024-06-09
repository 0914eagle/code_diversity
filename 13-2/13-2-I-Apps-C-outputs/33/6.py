
def get_boss_and_subordinates(employees, query):
    # Find the employee with the given ID
    employee = next((emp for emp in employees if emp[0] == query), None)
    if employee is None:
        return (0, 0)

    # Find the employee's boss
    boss = next((emp for emp in employees if emp[0] != query and emp[1] > employee[1] and emp[2] >= employee[2]), None)
    if boss is None:
        return (0, 0)

    # Find the employee's subordinates
    subordinates = [emp for emp in employees if emp[0] != query and emp[1] < employee[1] and emp[2] >= employee[2]]

    return (boss[0], len(subordinates))

def main():
    m, q = map(int, input().split())
    employees = []
    for _ in range(m):
        employees.append(tuple(map(int, input().split())))
    for _ in range(q):
        query = int(input())
        print(*get_boss_and_subordinates(employees, query))

if __name__ == '__main__':
    main()

