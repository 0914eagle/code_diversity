
import sys

def get_boss_and_subordinates(employees, query):
    boss = None
    subordinates = 0
    for employee in employees:
        if employee[0] == query:
            boss = employee[1]
            subordinates = employee[2]
            break
    return boss, subordinates

employees = []
m, q = map(int, input().split())
for i in range(m):
    employee_id, salary, height = map(int, input().split())
    employees.append((employee_id, salary, height))

for i in range(q):
    query = int(input())
    boss, subordinates = get_boss_and_subordinates(employees, query)
    print(boss, subordinates)

