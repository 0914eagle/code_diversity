
def get_vertical_dominoes(n, s):
    # Initialize variables
    vertical_dominoes = 0
    dominoes_pushed = [0] * n
    
    # Iterate through the string of pushed dominoes
    for i in range(n):
        # If the domino has been pushed to the left, push the domino to the left and the domino to the right
        if s[i] == "L":
            dominoes_pushed[i] = 1
            if i < n - 1 and dominoes_pushed[i + 1] == 0:
                dominoes_pushed[i + 1] = 1
        # If the domino has been pushed to the right, push the domino to the right and the domino to the left
        elif s[i] == "R":
            dominoes_pushed[i] = 1
            if i > 0 and dominoes_pushed[i - 1] == 0:
                dominoes_pushed[i - 1] = 1
    
    # Count the number of vertical dominoes
    for i in range(n):
        if dominoes_pushed[i] == 0:
            vertical_dominoes += 1
    
    return vertical_dominoes

def main():
    n = int(input())
    s = input()
    print(get_vertical_dominoes(n, s))

if __name__ == '__main__':
    main()

