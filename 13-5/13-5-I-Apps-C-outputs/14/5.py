
def f1(L, n):
    # f1 function to check if the wire would touch itself during the bending
    # L: length of the wire
    # n: number of points
    # return: 'GHOST' if the wire would touch itself, 'SAFE' otherwise

    # initialize the wire as a list of zeros and ones, where 0 represents a straight segment and 1 represents a bend
    wire = [0] * (L + 1)

    # iterate through the list of points and bends
    for i in range(n):
        # read the point and direction from the input
        point, direction = map(int, input().split())

        # check if the bend would cause the wire to touch itself
        if direction == 'C' and wire[point] == 1:
            return 'GHOST'
        elif direction == 'W' and wire[point] == 1 and wire[point - 1] == 1:
            return 'GHOST'

        # update the wire list with the new bend
        wire[point] = 1
        if direction == 'W':
            wire[point - 1] = 1

    # if the wire does not touch itself, return 'SAFE'
    return 'SAFE'

def f2(L, n):
    # f2 function to read the input and call f1 function
    # L: length of the wire
    # n: number of points
    # return: the output of f1 function

    # read the input
    points = []
    for i in range(n):
        points.append(list(map(int, input().split())))

    # call f1 function with the input
    return f1(L, n, points)

if __name__ == '__main__':
    # read the input
    L, n = map(int, input().split())

    # call f2 function with the input
    print(f2(L, n))

