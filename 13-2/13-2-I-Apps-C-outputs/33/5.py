
def get_boss_and_subordinates(employees, query):
    bosses = {}
    subordinates = {}
    for employee in employees:
        bosses[employee[0]] = employee[1]
        subordinates[employee[1]] = subordinates.get(employee[1], []) + [employee[0]]
    
    boss = bosses[query]
    subordinates = subordinates.get(query, [])
    return boss, len(subordinates)

def main():
    m, q = map(int, input().split())
    employees = []
    for i in range(m):
        employee = list(map(int, input().split()))
        employees.append(employee)
    
    for i in range(q):
        query = int(input())
        boss, subordinates = get_boss_and_subordinates(employees, query)
        print(boss, subordinates)

if __name__ == '__main__':
    main()

