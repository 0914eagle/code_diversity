
def get_number_of_standing_dominoes(n, s):
    # Initialize variables
    standing_dominoes = 0
    dominoes_fallen = 0
    dominoes_pushed_left = 0
    dominoes_pushed_right = 0

    # Iterate through the dominoes
    for i in range(n):
        # Check if the domino has been pushed left or right
        if s[i] == "L":
            dominoes_pushed_left += 1
        elif s[i] == "R":
            dominoes_pushed_right += 1

        # Check if the domino is standing vertically
        if s[i] == "." or (s[i] == "L" and i + 1 < n and s[i + 1] == "R") or (s[i] == "R" and i + 1 < n and s[i + 1] == "L"):
            standing_dominoes += 1
        else:
            dominoes_fallen += 1

    # Return the number of standing dominoes
    return standing_dominoes

def main():
    n = int(input())
    s = input()
    print(get_number_of_standing_dominoes(n, s))

if __name__ == '__main__':
    main()

