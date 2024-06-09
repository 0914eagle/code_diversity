
def f1(m, my_id, employees):
    # Initialize the number of employees to invite
    k = 0
    # Initialize the set of employees to invite
    invitees = set()
    # Iterate over the teams
    for i in range(m):
        # If the team has both employees from the same city, skip it
        if employees[i][0] // 1000 == employees[i][1] // 1000:
            continue
        # If the team has at least one employee from the other city, add the other employee to the set of invitees
        if employees[i][0] // 1000 != my_id // 1000:
            invitees.add(employees[i][0])
        if employees[i][1] // 1000 != my_id // 1000:
            invitees.add(employees[i][1])
    # If the set of invitees is empty, return 0
    if not invitees:
        return 0
    # Return the size of the set of invitees
    return len(invitees)

def f2(m, my_id, employees):
    # Initialize the number of employees to invite
    k = 0
    # Initialize the set of employees to invite
    invitees = set()
    # Iterate over the teams
    for i in range(m):
        # If the team has both employees from the same city, skip it
        if employees[i][0] // 1000 == employees[i][1] // 1000:
            continue
        # If the team has at least one employee from the other city, add the other employee to the set of invitees
        if employees[i][0] // 1000 != my_id // 1000:
            invitees.add(employees[i][0])
        if employees[i][1] // 1000 != my_id // 1000:
            invitees.add(employees[i][1])
    # If the set of invitees is empty, return 0
    if not invitees:
        return 0
    # Return the size of the set of invitees
    return len(invitees)

if __name__ == '__main__':
    m = int(input())
    my_id = int(input())
    employees = []
    for i in range(m):
        employees.append(list(map(int, input().split())))
    print(f1(m, my_id, employees))
    print(f2(m, my_id, employees))

