
def get_standing_dominoes(n, s):
    # Initialize variables
    standing_dominoes = 0
    left_dominoes = 0
    right_dominoes = 0

    # Iterate through the dominoes
    for i in range(n):
        # Check if the domino has been pushed to the left
        if s[i] == "L":
            left_dominoes += 1
        # Check if the domino has been pushed to the right
        elif s[i] == "R":
            right_dominoes += 1
        # Check if the domino is standing vertically
        else:
            standing_dominoes += 1

    # Iterate through the dominoes again
    for i in range(n):
        # Check if the domino is standing vertically
        if s[i] == ".":
            # Check if the dominoes on the left and right are balanced
            if left_dominoes == right_dominoes:
                standing_dominoes += 1
            # Check if the dominoes on the left are greater than the dominoes on the right
            elif left_dominoes > right_dominoes:
                standing_dominoes += 1
                left_dominoes -= 1
            # Check if the dominoes on the right are greater than the dominoes on the left
            else:
                standing_dominoes += 1
                right_dominoes -= 1

    return standing_dominoes

def main():
    n = int(input())
    s = input()
    print(get_standing_dominoes(n, s))

if __name__ == '__main__':
    main()

