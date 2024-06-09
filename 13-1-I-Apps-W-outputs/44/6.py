
def solve(s):
    # Initialize a 10x10 matrix to store the results
    matrix = [[0] * 10 for _ in range(10)]

    # Iterate over all possible values of x and y
    for x in range(10):
        for y in range(10):
            # Initialize a variable to store the current value of the counter
            value = 0

            # Iterate over the remaining digits of the sequence
            for i in range(len(s)):
                # If the current digit is equal to the lowest digit of the counter, print it and add x to the value
                if s[i] == str(value % 10):
                    matrix[x][y] += 1
                    value += x

                # If the current digit is not equal to the lowest digit of the counter, print it and add y to the value
                else:
                    matrix[x][y] += 1
                    value += y

    return matrix

