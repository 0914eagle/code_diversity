
def get_immediate_boss(employees, employee_id):
    for employee in employees:
        if employee["id"] == employee_id:
            return employee["boss_id"]
    return 0

def get_subordinates(employees, employee_id):
    subordinates = []
    for employee in employees:
        if employee["boss_id"] == employee_id:
            subordinates.append(employee["id"])
    return subordinates

def main():
    employees = []
    while True:
        try:
            line = input()
            if not line:
                break
            employee_id, salary, height = map(int, line.split())
            employees.append({"id": employee_id, "salary": salary, "height": height})
        except EOFError:
            break
    
    queries = []
    while True:
        try:
            line = input()
            if not line:
                break
            queries.append(int(line))
        except EOFError:
            break
    
    for query in queries:
        boss_id = get_immediate_boss(employees, query)
        subordinates = get_subordinates(employees, query)
        print(boss_id, len(subordinates))

if __name__ == '__main__':
    main()

