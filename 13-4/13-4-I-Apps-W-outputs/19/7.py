
def read_input():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    return H, W, S

def find_starting_square(S):
    for i in range(len(S)):
        for j in range(len(S[0])):
            if S[i][j] == '.':
                return i, j
    return -1, -1

def find_goal_square(S):
    for i in range(len(S)):
        for j in range(len(S[0])):
            if S[i][j] == '.':
                return i, j
    return -1, -1

def find_min_moves(start, goal):
    # Implement your solution here
    pass

def main():
    H, W, S = read_input()
    start = find_starting_square(S)
    goal = find_goal_square(S)
    print(find_min_moves(start, goal))

if __name__ == '__main__':
    main()

