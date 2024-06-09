
def f1(P):
    # Initialize variables
    ones = 0
    twos = 0
    threes = 0
    fours = 0
    fives = 0
    total = 0

    # Calculate the average
    average = P / 5

    # Loop through the numbers from 1 to 5
    for i in range(1, 6):
        # Calculate the number of pieces of paper needed for each number
        num_pieces = int(average // i)
        total += num_pieces

        # Add the number of pieces to the corresponding variable
        if i == 1:
            ones = num_pieces
        elif i == 2:
            twos = num_pieces
        elif i == 3:
            threes = num_pieces
        elif i == 4:
            fours = num_pieces
        else:
            fives = num_pieces

    # Return the solution
    return [ones, twos, threes, fours, fives]

def f2(P):
    # Initialize variables
    ones = 0
    twos = 0
    threes = 0
    fours = 0
    fives = 0
    total = 0

    # Calculate the average
    average = P / 5

    # Loop through the numbers from 1 to 5
    for i in range(1, 6):
        # Calculate the number of pieces of paper needed for each number
        num_pieces = int(average // i)
        total += num_pieces

        # Add the number of pieces to the corresponding variable
        if i == 1:
            ones = num_pieces
        elif i == 2:
            twos = num_pieces
        elif i == 3:
            threes = num_pieces
        elif i == 4:
            fours = num_pieces
        else:
            fives = num_pieces

    # Return the solution
    return [ones, twos, threes, fours, fives]

if __name__ == '__main__':
    P = float(input())
    print(f1(P))
    print(f2(P))

