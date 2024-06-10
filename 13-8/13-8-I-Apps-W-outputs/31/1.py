
def get_standing_dominoes(n, s):
    # Initialize variables
    standing_dominoes = 0
    dominoes_fallen = 0
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
        # Check if the domino has not been pushed
        else:
            # Check if the dominoes on both sides are standing
            if left_dominoes > 0 and right_dominoes > 0:
                standing_dominoes += 1
            # Check if the dominoes on both sides have fallen
            elif left_dominoes == 0 and right_dominoes == 0:
                dominoes_fallen += 1
            # Check if the domino is the first one and has not been pushed
            elif i == 0 and s[i] == ".":
                standing_dominoes += 1

    # Return the number of standing dominoes
    return standing_dominoes

def main():
    n = int(input())
    s = input()
    result = get_standing_dominoes(n, s)
    print(result)

if __name__ == '__main__':
    main()

