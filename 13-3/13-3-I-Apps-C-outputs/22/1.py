
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
for _ in range(int(input())):
    employees.append(list(map(int, input().split())))

for query in map(int, input().split()):
    boss, subordinates = get_boss_and_subordinates(employees, query)
    print(boss, subordinates)

