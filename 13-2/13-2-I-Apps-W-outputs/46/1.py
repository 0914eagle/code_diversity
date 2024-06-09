
def f1(t, pieces):
    # Initialize a dictionary to store the number of instances for each digit
    instances = {digit: 0 for digit in range(10)}

    # Iterate through the pieces of ice
    for piece in pieces:
        # If the piece is 6 or 9, rotate it to get the other digit
        if piece in [6, 9]:
            piece = 9 if piece == 6 else 6

        # If the piece is 2 or 5, rotate it to get the other digit
        elif piece in [2, 5]:
            piece = 5 if piece == 2 else 2

        # Increment the number of instances for the current digit
        instances[piece] += 1

    # Return the number of instances for the target digit
    return instances[t]

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    t = int(input())
    pieces = input()
    print(f1(t, pieces))

