
def f1(n, c, encounters):
    # f1(n, c, encounters) should return the smallest year Y such that it is possible to divide the participants in two parts, neither of which contains more than 2n/3 people, such that all people in the first part first met before year Y, and all people in the second part first met in or after year Y.
    # If there is no such year, f1(n, c, encounters) should return the string 'Impossible'.

    # Initialize a dictionary to keep track of the first encounters
    first_encounters = {}
    for a, b, y in encounters:
        first_encounters[(a, b)] = y

    # Sort the encounters by year in ascending order
    sorted_encounters = sorted(encounters, key=lambda x: x[2])

    # Initialize the minimum year Y and the number of people in each part
    Y = 1948
    num_people_part1 = 0
    num_people_part2 = 0

    # Loop through the encounters and check if it is possible to divide the participants in two parts
    for a, b, y in sorted_encounters:
        if y <= Y:
            num_people_part1 += 1
        else:
            num_people_part2 += 1
        if num_people_part1 > 2 * n / 3 or num_people_part2 > 2 * n / 3:
            return 'Impossible'

    return Y

def f2(...):
    # f2(...) should return ...
    ...

if __name__ == '__main__':
    n = int(input())
    c = int(input())
    encounters = []
    for _ in range(c):
        a, b, y = map(int, input().split())
        encounters.append((a, b, y))
    result = f1(n, c, encounters)
    print(result)

