
def get_boss_and_subordinates(employees, query):
    bosses = {}
    subordinates = {}
    for employee in employees:
        bosses[employee[0]] = employee[1]
        subordinates[employee[0]] = employee[2]
    
    for employee in employees:
        if employee[0] in bosses:
            bosses[employee[1]] = employee[0]
            subordinates[employee[1]] += 1
    
    return bosses[query], subordinates[query]

