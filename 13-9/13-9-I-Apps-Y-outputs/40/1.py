
def get_optimal_position(S):
    # find the longest common prefix of S and S[1:]
    lcp = ""
    for i in range(len(S)):
        if S.startswith(S[i:]):
            lcp = S[:i+1]
    # return the length of the longest common prefix
    return len(lcp)

def solve(S):
    # find the optimal position
    position = get_optimal_position(S)
    # split the string at the optimal position
    X = S[:position]
    Y = S[position:]
    # count the number of different letters in both X and Y
    count = 0
    for c in X:
        if c not in Y:
            count += 1
    for c in Y:
        if c not in X:
            count += 1
    # return the result
    return count

if __name__ == '__main__':
    # read a single line of input from stdin and convert it to an integer
    N = int(input().strip())
    # read a single line of input from stdin and save it in a variable
    S = input().strip()
    # call the solve function and save the result in a variable
    result = solve(S)
    # print the result
    print(result)

