
def get_boss_and_subordinates(employees, query):
    # Find the employee with the given ID
    employee = next((emp for emp in employees if emp["id"] == query), None)
    if employee is None:
        return (0, 0)

    # Find the employee's boss
    boss = next((emp for emp in employees if emp["height"] >= employee["height"] and emp["salary"] > employee["salary"]), None)
    if boss is None:
        return (0, 0)

    # Find the employee's subordinates
    subordinates = [emp for emp in employees if emp["height"] >= employee["height"] and emp["salary"] > employee["salary"] and emp["id"] != employee["id"]]

    return (boss["id"], len(subordinates))

def main():
    m, q = map(int, input().split())
    employees = []
    for _ in range(m):
        employee = {"id": int(input()), "salary": int(input()), "height": int(input())}
        employees.append(employee)
    for _ in range(q):
        query = int(input())
        boss, subordinates = get_boss_and_subordinates(employees, query)
        print(boss, subordinates)

if __name__ == '__main__':
    main()

