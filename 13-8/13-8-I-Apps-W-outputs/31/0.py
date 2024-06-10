
def count_standing_dominoes(n, s):
    # Initialize variables
    standing_dominoes = 0
    left_pushed_dominoes = 0
    right_pushed_dominoes = 0

    # Iterate through the dominoes
    for i in range(n):
        # Check if the domino has been pushed to the left
        if s[i] == "L":
            left_pushed_dominoes += 1
        # Check if the domino has been pushed to the right
        elif s[i] == "R":
            right_pushed_dominoes += 1
        # Check if the domino is standing vertically
        elif left_pushed_dominoes > 0 and right_pushed_dominoes > 0:
            standing_dominoes += 1
            left_pushed_dominoes -= 1
            right_pushed_dominoes -= 1

    return standing_dominoes

def main():
    n = int(input())
    s = input()
    print(count_standing_dominoes(n, s))

if __name__ == '__main__':
    main()

