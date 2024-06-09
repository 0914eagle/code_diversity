
def get_max_score(N, M, Q, a, b, c, d):
    # Initialize the sequence with the first element as 1
    seq = [1]
    # Initialize the score to 0
    score = 0
    # Loop through each quadruple (a_i, b_i, c_i, d_i)
    for i in range(Q):
        # If the sequence is not long enough, extend it with the next element
        if len(seq) < b[i]:
            seq.append(seq[-1] + 1)
        # If the sequence is long enough, but the next element is not in the correct position, insert it
        elif seq[b[i] - 1] != seq[a[i] - 1] + c[i]:
            seq.insert(b[i], seq[a[i] - 1] + c[i])
        # If the sequence is already correct, just update the score
        else:
            score += d[i]
    # Return the maximum possible score
    return score

def main():
    # Read the input from stdin
    N, M, Q = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d = list(map(int, input().split()))
    # Call the function to get the maximum possible score
    score = get_max_score(N, M, Q, a, b, c, d)
    # Print the result
    print(score)

if __name__ == '__main__':
    main()

