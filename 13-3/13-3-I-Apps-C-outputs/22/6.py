
import sys

def get_immediate_boss(employees, employee_id):
    for employee in employees:
        if employee[0] == employee_id:
            return employee[1]
    return 0

def get_subordinates(employees, employee_id):
    subordinates = 0
    for employee in employees:
        if employee[1] == employee_id:
            subordinates += 1
    return subordinates

m, q = map(int, input().split())
employees = []
for i in range(m):
    employee_id, salary, height = map(int, input().split())
    employees.append((employee_id, salary, height))

for i in range(q):
    employee_id = int(input())
    boss_id = get_immediate_boss(employees, employee_id)
    subordinates = get_subordinates(employees, employee_id)
    print(boss_id, subordinates)

