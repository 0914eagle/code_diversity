
def f1(n, c, encounters):
    # f1(n, c, encounters) should return the smallest year Y such that it is possible to divide the participants in two parts, neither of which contains more than 2n/3 people, such that all people in the first part first met before year Y, and all people in the second part first met in or after year Y.
    # If there is no such year, f1(n, c, encounters) should return the string 'Impossible'.

    # Initialize a dictionary to keep track of the first encounters
    first_encounters = {}
    for a, b, y in encounters:
        if a not in first_encounters:
            first_encounters[a] = []
        first_encounters[a].append((b, y))

    # Sort the first encounters by year in ascending order
    for key in first_encounters:
        first_encounters[key].sort(key=lambda x: x[1])

    # Initialize the smallest year Y and the number of people in each part
    Y = 1948
    num_people_part1 = 0
    num_people_part2 = 0

    # Iterate through the first encounters and check if it is possible to divide the participants in two parts
    for a in range(1, n + 1):
        if a in first_encounters:
            # Check if the current person has any first encounters before year Y
            for b, y in first_encounters[a]:
                if y < Y:
                    num_people_part1 += 1
                    break
            else:
                # If the current person has no first encounters before year Y, add them to part 2
                num_people_part2 += 1
        else:
            # If the current person has no first encounters, add them to part 2
            num_people_part2 += 1

        # Check if the number of people in each part is more than 2n/3
        if num_people_part1 > 2 * n / 3 or num_people_part2 > 2 * n / 3:
            return 'Impossible'

        # If the number of people in each part is less than or equal to 2n/3, increase the year Y by 1
        Y += 1

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

