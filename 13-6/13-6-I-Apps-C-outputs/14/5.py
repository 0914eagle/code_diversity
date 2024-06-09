
def get_smallest_number_of_people_to_invite(teams):
    # Initialize a set to store the IDs of the employees to invite
    invited_employees = set()
    # Initialize a variable to store the smallest number of people to invite
    smallest_number_of_people = float('inf')
    # Loop through each team
    for team in teams:
        # If the first employee of the team is not already in the set of invited employees, add them to the set
        if team[0] not in invited_employees:
            invited_employees.add(team[0])
        # If the second employee of the team is not already in the set of invited employees, add them to the set
        if team[1] not in invited_employees:
            invited_employees.add(team[1])
        # If the size of the set of invited employees is equal to the smallest number of people to invite, break the loop
        if len(invited_employees) == smallest_number_of_people:
            break
        # If the size of the set of invited employees is smaller than the smallest number of people to invite, update the smallest number of people to invite
        if len(invited_employees) < smallest_number_of_people:
            smallest_number_of_people = len(invited_employees)
    # Return the smallest number of people to invite
    return smallest_number_of_people

def get_list_of_employees_to_invite(teams, smallest_number_of_people):
    # Initialize a set to store the IDs of the employees to invite
    invited_employees = set()
    # Loop through each team
    for team in teams:
        # If the first employee of the team is not already in the set of invited employees, add them to the set
        if team[0] not in invited_employees:
            invited_employees.add(team[0])
        # If the second employee of the team is not already in the set of invited employees, add them to the set
        if team[1] not in invited_employees:
            invited_employees.add(team[1])
        # If the size of the set of invited employees is equal to the smallest number of people to invite, break the loop
        if len(invited_employees) == smallest_number_of_people:
            break
    # Return the list of employees to invite
    return list(invited_employees)

def main():
    # Read the number of teams from stdin
    number_of_teams = int(input())
    # Read the teams from stdin
    teams = []
    for _ in range(number_of_teams):
        teams.append(list(map(int, input().split())))
    # Get the smallest number of people to invite
    smallest_number_of_people = get_smallest_number_of_people_to_invite(teams)
    # Get the list of employees to invite
    employees_to_invite = get_list_of_employees_to_invite(teams, smallest_number_of_people)
    # Print the number of people to invite
    print(smallest_number_of_people)
    # Print the list of employees to invite
    for employee in employees_to_invite:
        print(employee)

if __name__ == '__main__':
    main()

