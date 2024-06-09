
def f1(n, c, encounters):
    # f1(n, c, encounters) should return the smallest year Y such that it is possible to divide the participants in two parts, neither of which contains more than 2n/3 people, such that all people in the first part first met before year Y, and all people in the second part first met in or after year Y.
    # If there is no such year, f1(n, c, encounters) should return the string 'Impossible'.
    
    # Initialize a dictionary to store the first encounters of each pair of participants
    first_encounters = {}
    for a, b, y in encounters:
        if (a, b) not in first_encounters:
            first_encounters[(a, b)] = y
        elif first_encounters[(a, b)] > y:
            first_encounters[(a, b)] = y
    
    # Initialize a set to store the participants who have not met anyone yet
    unmet = set(range(1, n+1))
    
    # Initialize a list to store the participants who have met someone
    met = []
    
    # Initialize a variable to store the smallest year Y
    Y = 2008
    
    # Loop through the dictionary of first encounters and update the set of unmet participants and the list of met participants
    for pair, y in first_encounters.items():
        if y < Y:
            Y = y
        if pair[0] in unmet:
            unmet.remove(pair[0])
            met.append(pair[0])
        if pair[1] in unmet:
            unmet.remove(pair[1])
            met.append(pair[1])
    
    # If there are still unmet participants, it is not possible to divide the participants into two parts that meet the criteria
    if len(unmet) > 0:
        return 'Impossible'
    
    # If there are no unmet participants, return the smallest year Y
    return Y

def f2(...):
    # f2(...) should return ...
    ...

if __name__ == '__main__':
    n = int(input())
    c = int(input())
    encounters = []
    for i in range(c):
        a, b, y = map(int, input().split())
        encounters.append((a, b, y))
    result = f1(n, c, encounters)
    print(result)

