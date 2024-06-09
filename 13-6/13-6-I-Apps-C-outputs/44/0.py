
def f1(n, k, circle):
    # f1 function to count the number of distinct starting circles
    # that give the same circle after k transformations as Stanko's original circle does
    # n: number of pebbles in the circle
    # k: number of transformations made by Stanko
    # circle: the configuration of the circle before Stanko performed the transformation

    # initialize a dictionary to store the number of occurrences of each starting circle
    circle_count = {}

    # iterate through all possible starting circles
    for i in range(n):
        # get the starting circle by rotating the original circle i positions
        starting_circle = circle[i:] + circle[:i]

        # if the starting circle is not in the dictionary, add it to the dictionary with a count of 1
        if starting_circle not in circle_count:
            circle_count[starting_circle] = 1
        # if the starting circle is already in the dictionary, increment its count
        else:
            circle_count[starting_circle] += 1

    # return the number of distinct starting circles
    return len(circle_count)

def f2(n, k, circle):
    # f2 function to determine the number of possible starting circles
    # that give the same circle after k transformations as Stanko's original circle does
    # n: number of pebbles in the circle
    # k: number of transformations made by Stanko
    # circle: the configuration of the circle before Stanko performed the transformation

    # initialize a set to store the possible starting circles
    possible_circles = set()

    # iterate through all possible starting circles
    for i in range(n):
        # get the starting circle by rotating the original circle i positions
        starting_circle = circle[i:] + circle[:i]

        # add the starting circle to the set of possible starting circles
        possible_circles.add(starting_circle)

    # return the number of possible starting circles
    return len(possible_circles)

if __name__ == '__main__':
    # read the input from stdin
    n, k = map(int, input().split())
    circle = input()

    # call f1 function to count the number of distinct starting circles
    distinct_circles = f1(n, k, circle)

    # call f2 function to determine the number of possible starting circles
    possible_circles = f2(n, k, circle)

    # print the number of possible starting circles
    print(possible_circles)

