
def f1(N, K, circle):
    # f1 function to count the number of distinct starting circles
    # that give the same circle after K transformations as Stanko's original circle does
    # N: number of pebbles in the circle
    # K: number of transformations made by Stanko
    # circle: the configuration of the circle before Stanko performed the transformation

    # initialize a set to store the distinct starting circles
    starting_circles = set()

    # loop through each possible starting circle
    for i in range(N):
        # create a copy of the starting circle
        current_circle = circle[:]
        # loop through each transformation
        for j in range(K):
            # find the index of the first black pebble
            black_index = current_circle.index("B")
            # find the index of the first white pebble
            white_index = current_circle.index("W")
            # check if the black pebble is to the left of the white pebble
            if black_index < white_index:
                # insert a black pebble between the black pebble and the white pebble
                current_circle.insert(black_index + 1, "B")
                # remove the first black pebble
                current_circle.pop(0)
            else:
                # insert a white pebble between the black pebble and the white pebble
                current_circle.insert(black_index + 1, "W")
                # remove the first white pebble
                current_circle.pop(0)
        # add the current circle to the set of starting circles
        starting_circles.add(tuple(current_circle))

    # return the number of distinct starting circles
    return len(starting_circles)

def f2(N, K, circle):
    # f2 function to count the number of distinct starting circles
    # that give the same circle after K transformations as Stanko's original circle does
    # N: number of pebbles in the circle
    # K: number of transformations made by Stanko
    # circle: the configuration of the circle before Stanko performed the transformation

    # initialize a set to store the distinct starting circles
    starting_circles = set()

    # loop through each possible starting circle
    for i in range(N):
        # create a copy of the starting circle
        current_circle = circle[:]
        # loop through each transformation
        for j in range(K):
            # find the index of the first black pebble
            black_index = current_circle.index("B")
            # find the index of the first white pebble
            white_index = current_circle.index("W")
            # check if the black pebble is to the left of the white pebble
            if black_index < white_index:
                # insert a black pebble between the black pebble and the white pebble
                current_circle.insert(black_index + 1, "B")
                # remove the first black pebble
                current_circle.pop(0)
            else:
                # insert a white pebble between the black pebble and the white pebble
                current_circle.insert(black_index + 1, "W")
                # remove the first white pebble
                current_circle.pop(0)
        # add the current circle to the set of starting circles
        starting_circles.add(tuple(current_circle))

    # return the number of distinct starting circles
    return len(starting_circles)

if __name__ == '__main__':
    # read the input
    N, K = map(int, input().split())
    circle = list(input())

    # call the f1 function to count the number of distinct starting circles
    result1 = f1(N, K, circle)
    # call the f2 function to count the number of distinct starting circles
    result2 = f2(N, K, circle)

    # print the number of distinct starting circles
    print(result1)
    print(result2)

