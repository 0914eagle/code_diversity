
def get_initial_arrangement(n, x, a):
    # Initialize an array to store the initial arrangement of balls
    initial_arrangement = [0] * n

    # Initialize a variable to keep track of the number of balls left
    num_balls_left = sum(a)

    # Loop through each box and its corresponding number of balls
    for i in range(n):
        # If the current box is the last box that Vasya put a ball in,
        # then the number of balls in the current box is the number of balls left
        if i == x - 1:
            initial_arrangement[i] = num_balls_left
            break
        # Otherwise, the number of balls in the current box is the sum of the number of balls in the current box and the next box
        else:
            initial_arrangement[i] = a[i] + a[(i + 1) % n]
            num_balls_left -= a[i]

    return initial_arrangement

