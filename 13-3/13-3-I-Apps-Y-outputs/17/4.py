
def get_max_score(N, M, Q, quadruples):
    # Initialize the sequence with the first element as 1
    seq = [1]
    # Initialize the score to 0
    score = 0
    # Loop through the quadruples
    for a, b, c, d in quadruples:
        # If the sequence is not long enough, extend it with the next element
        if len(seq) < b:
            seq.append(seq[-1] + 1)
        # If the sequence is long enough, but the next element is not the correct one, replace it
        if len(seq) == b and seq[b-1] != c+1:
            seq[b-1] = c+1
        # If the sequence is long enough and the next element is the correct one, update the score
        if len(seq) == b and seq[b-1] == c+1:
            score += d
    # Return the maximum possible score
    return score

def main():
    # Read the input from stdin
    N, M, Q = map(int, input().split())
    quadruples = []
    for _ in range(Q):
        a, b, c, d = map(int, input().split())
        quadruples.append((a, b, c, d))
    # Call the function to get the maximum possible score
    score = get_max_score(N, M, Q, quadruples)
    # Print the result
    print(score)

if __name__ == '__main__':
    main()

