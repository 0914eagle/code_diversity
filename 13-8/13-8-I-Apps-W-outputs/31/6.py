
def get_vertically_standing_dominoes(n, s):
    # Initialize variables
    standing_dominoes = 0
    falling_dominoes = 0
    left_pushed_dominoes = 0
    right_pushed_dominoes = 0

    # Iterate through the string
    for i in range(n):
        if s[i] == "L":
            left_pushed_dominoes += 1
        elif s[i] == "R":
            right_pushed_dominoes += 1

        # Check if the domino is standing vertically
        if left_pushed_dominoes == right_pushed_dominoes:
            standing_dominoes += 1

        # Check if the domino is falling to the left or right
        if left_pushed_dominoes > right_pushed_dominoes:
            falling_dominoes += left_pushed_dominoes - right_pushed_dominoes
        elif right_pushed_dominoes > left_pushed_dominoes:
            falling_dominoes += right_pushed_dominoes - left_pushed_dominoes

    return standing_dominoes

def main():
    n = int(input())
    s = input()
    result = get_vertically_standing_dominoes(n, s)
    print(result)

if __name__ == '__main__':
    main()

