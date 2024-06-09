
def get_boss_and_subordinates(employees, query):
    bosses = {}
    subordinates = {}

    for employee in employees:
        bosses[employee[0]] = employee[1]
        subordinates[employee[1]] = subordinates.get(employee[1], []) + [employee[0]]

    boss = bosses[query]
    subordinates = subordinates.get(query, [])

    return boss, len(subordinates)

employees = [(123456, 14323, 1700000), (123458, 41412, 1900000), (123457, 15221, 1800000)]
query = 123456

boss, subordinates = get_boss_and_subordinates(employees, query)
print(boss, subordinates)

