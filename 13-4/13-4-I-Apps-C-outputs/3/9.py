
employees = []

def get_boss_and_subordinates(employee_id):
    boss_id = 0
    subordinates = 0
    for employee in employees:
        if employee[0] == employee_id:
            boss_id = employee[1]
            subordinates = employee[2]
            break
    return boss_id, subordinates

m, q = map(int, input().split())
for i in range(m):
    employee_id, salary, height = map(int, input().split())
    employees.append([employee_id, salary, height])

for i in range(q):
    employee_id = int(input())
    boss_id, subordinates = get_boss_and_subordinates(employee_id)
    print(boss_id, subordinates)
