
def get_max_score(N, M, Q, quadruples):
    # Initialize the sequence with the first element as 1
    seq = [1]
    # Initialize the score to 0
    score = 0
    # Iterate through the quadruples
    for a, b, c, d in quadruples:
        # If the sequence is not long enough, extend it with the next element
        if len(seq) < b:
            seq.append(seq[-1] + 1)
        # If the sequence is long enough, check if the difference between the elements at positions a and b is equal to c
        if seq[b - 1] - seq[a - 1] == c:
            # If it is, add the score to the current score
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

