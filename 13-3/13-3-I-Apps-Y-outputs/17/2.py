
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
        # If the sequence is long enough, but the next element is not the correct value, replace it
        if len(seq) >= b and seq[b - 1] != c + 1:
            seq[b - 1] = c + 1
        # If the sequence is long enough and the next element is the correct value, update the score
        if len(seq) >= b and seq[b - 1] == c + 1:
            score += d
    # Return the maximum possible score
    return score

def main():
    # Read the input from stdin
    N, M, Q = map(int, input().split())
    quadruples = [tuple(map(int, input().split())) for _ in range(Q)]
    # Call the function to get the maximum possible score
    score = get_max_score(N, M, Q, quadruples)
    # Print the result
    print(score)

if __name__ == '__main__':
    main()

