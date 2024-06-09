
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
    m, q = map(int, input().split())
    employees = []
    for i in range(m):
        employee_id, salary, height = map(int, input().split())
        employees.append({"id": employee_id, "salary": salary, "height": height})
    
    for i in range(q):
        employee_id = int(input())
        boss_id = get_immediate_boss(employees, employee_id)
        subordinates = get_subordinates(employees, employee_id)
        print(boss_id, len(subordinates))

if __name__ == "__main__":
    main()

