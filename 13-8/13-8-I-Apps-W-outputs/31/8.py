
def push_dominoes(n, s):
    # Initialize variables
    standing_dominoes = 0
    direction = [0] * n
    for i in range(n):
        if s[i] == "L":
            direction[i] = -1
        elif s[i] == "R":
            direction[i] = 1
    
    # Simulate the dominoes falling
    for i in range(n):
        if direction[i] != 0:
            standing_dominoes += 1
        if i < n - 1 and direction[i] != direction[i + 1]:
            standing_dominoes -= 1
    
    return standing_dominoes

def main():
    n = int(input())
    s = input()
    print(push_dominoes(n, s))

if __name__ == '__main__':
    main()

