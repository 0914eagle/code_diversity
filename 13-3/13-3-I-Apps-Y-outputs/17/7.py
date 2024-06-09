
def get_max_score(N, M, Q, quadruples):
    # Initialize the sequence with the first element as 1
    seq = [1]
    # Initialize the score to 0
    score = 0
    # Loop through each quadruple
    for a, b, c, d in quadruples:
        # If the sequence is not long enough, extend it
        if len(seq) < b:
            seq.extend([x + 1 for x in range(len(seq), b)])
        # If the sequence is long enough, but the last element is not M, extend it
        if len(seq) == b and seq[-1] < M:
            seq.append(seq[-1] + 1)
        # If the sequence is long enough and the last element is M, extend it with a new element
        if len(seq) == b and seq[-1] == M:
            seq.append(1)
        # If the sequence is long enough and the last element is not M, check if the difference between the elements at indices a and b is equal to c
        if len(seq) >= b and seq[b - 1] - seq[a - 1] == c:
            # If the difference is equal to c, add d to the score
            score += d
    # Return the maximum possible score
    return score

def main():
    # Read the input from stdin
    N, M, Q = map(int, input().split())
    quadruples = [list(map(int, input().split())) for _ in range(Q)]
    # Call the function to get the maximum possible score
    score = get_max_score(N, M, Q, quadruples)
    # Print the maximum possible score
    print(score)

if __name__ == '__main__':
    main()

