
def f1(m, my_id):
    # Initialize a set to store the IDs of the employees to invite
    invitees = set()
    # Initialize a dictionary to store the number of teams each employee is in
    num_teams = {}
    # Iterate over the input m teams
    for _ in range(m):
        # Read the input for the two employees in the team
        i, j = map(int, input().split())
        # If the first employee is not in the set of invitees, add them
        if i not in invitees:
            invitees.add(i)
            # If the first employee is not in the dictionary, add them with value 1
            if i not in num_teams:
                num_teams[i] = 1
            # If the first employee is already in the dictionary, increment their value
            else:
                num_teams[i] += 1
        # If the second employee is not in the set of invitees, add them
        if j not in invitees:
            invitees.add(j)
            # If the second employee is not in the dictionary, add them with value 1
            if j not in num_teams:
                num_teams[j] = 1
            # If the second employee is already in the dictionary, increment their value
            else:
                num_teams[j] += 1
    # Sort the dictionary by value in descending order
    sorted_num_teams = sorted(num_teams.items(), key=lambda x: x[1], reverse=True)
    # Initialize a variable to store the minimum number of employees to invite
    min_invitees = 0
    # Iterate over the sorted dictionary
    for employee, num_teams in sorted_num_teams:
        # If the current employee is not your friend, add them to the set of invitees
        if employee != my_id:
            invitees.add(employee)
        # Increment the minimum number of employees to invite
        min_invitees += 1
        # If the current employee is your friend, break the loop
        if employee == my_id:
            break
    return min_invitees, invitees

def f2(min_invitees, invitees):
    # Initialize a list to store the IDs of the employees to invite
    invitee_ids = []
    # Iterate over the set of invitees
    for invitee in invitees:
        # Add the ID of the current employee to the list
        invitee_ids.append(invitee)
    # Sort the list of IDs in ascending order
    invitee_ids.sort()
    # Return the list of IDs
    return invitee_ids

if __name__ == '__main__':
    # Read the input for the number of teams and your friend's ID
    m, my_id = map(int, input().split())
    # Call f1 to get the minimum number of employees to invite and the set of employees to invite
    min_invitees, invitees = f1(m, my_id)
    # Call f2 to get the list of IDs of the employees to invite
    invitee_ids = f2(min_invitees, invitees)
    # Print the minimum number of employees to invite
    print(min_invitees)
    # Print the list of IDs of the employees to invite
    print(*invitee_ids, sep='\n')

