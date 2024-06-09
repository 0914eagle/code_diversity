
def get_boss_and_subordinates(employees, query):
    # Find the employee with the given ID
    employee = next((e for e in employees if e["id"] == query), None)
    if employee is None:
        return (0, 0)

    # Find the employee's boss
    boss = next((e for e in employees if e["height"] >= employee["height"] and e["salary"] > employee["salary"]), None)
    if boss is None:
        return (0, 0)

    # Find the employee's subordinates
    subordinates = [e for e in employees if e["height"] >= employee["height"] and e["salary"] < employee["salary"] and e["boss"] == employee["id"]]

    return (boss["id"], len(subordinates))

employees = []
while True:
    try:
        id, salary, height = input().split()
        employees.append({"id": int(id), "salary": int(salary), "height": int(height)})
    except EOFError:
        break

queries = []
while True:
    try:
        queries.append(int(input()))
    except EOFError:
        break

for query in queries:
    boss, subordinates = get_boss_and_subordinates(employees, query)
    print(boss, subordinates)

