
def f1(m):
    # function to read the input file
    with open("input.txt", "r") as f:
        content = f.read().splitlines()
    # convert the input to a list of lists
    input_list = [list(map(int, line.split())) for line in content]
    return input_list

def f2(input_list):
    # function to find the smallest number of people to invite
    # initialize the number of people to invite as 0
    k = 0
    # initialize a set to store the IDs of the invited people
    invited = set()
    # loop through the input list
    for team in input_list:
        # if the team has both members from the same city, skip it
        if team[0] // 1000 == team[1] // 1000:
            continue
        # if the team has both members from different cities, add them to the set of invited people
        invited.add(team[0])
        invited.add(team[1])
        # increment the number of people to invite
        k += 2
    return k, invited

def f3(input_list, k, invited):
    # function to find the smallest subset of the input list that contains at least one member from each project
    # initialize a set to store the IDs of the projects
    projects = set()
    # loop through the input list
    for team in input_list:
        # if the team has both members from the same project, skip it
        if team[0] // 1000 == team[1] // 1000:
            continue
        # if the team has both members from different projects, add them to the set of projects
        projects.add(team[0] // 1000)
        projects.add(team[1] // 1000)
    # initialize a list to store the final output
    output = []
    # loop through the set of projects
    for project in projects:
        # loop through the input list
        for team in input_list:
            # if the team has both members from the same project, skip it
            if team[0] // 1000 == team[1] // 1000:
                continue
            # if the team has both members from different projects, add them to the output list
            if team[0] // 1000 == project or team[1] // 1000 == project:
                output.append(team)
                # decrement the number of people to invite
                k -= 1
                # if the number of people to invite reaches 0, break the loop
                if k == 0:
                    break
    return output

if __name__ == '__main__':
    # read the input file
    input_list = f1(m)
    # find the smallest number of people to invite
    k, invited = f2(input_list)
    # find the smallest subset of the input list that contains at least one member from each project
    output = f3(input_list, k, invited)
    # print the output
    print(k)
    for team in output:
        print(team[0], team[1])

