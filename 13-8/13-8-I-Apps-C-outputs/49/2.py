
def get_balls(n, t):
    # sort the list of ball sizes in ascending order
    t.sort()
    # initialize three variables to keep track of the chosen balls
    ball1, ball2, ball3 = 0, 0, 0
    # loop through the list of ball sizes
    for i in range(n):
        # check if the current ball is within the range of the previous two balls
        if t[i] - t[i-1] <= 2:
            # if it is, assign it to the third ball
            ball3 = t[i]
            break
        # if it is not, assign it to the first ball
        else:
            ball1 = t[i]
    # loop through the list of ball sizes again
    for i in range(n):
        # check if the current ball is within the range of the first two balls
        if t[i] - t[i-1] <= 2:
            # if it is, assign it to the third ball
            ball3 = t[i]
            break
        # if it is not, assign it to the second ball
        else:
            ball2 = t[i]
    # return the chosen balls
    return [ball1, ball2, ball3]

def main():
    # read the number of balls and the list of ball sizes from stdin
    n = int(input())
    t = list(map(int, input().split()))
    # get the chosen balls
    balls = get_balls(n, t)
    # print the result
    print("YES" if balls[0] != balls[1] and balls[1] != balls[2] and balls[2] != balls[0] else "NO")

if __name__ == '__main__':
    main()

