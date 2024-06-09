
def get_maximum_score(N, M, Q, quadruples):
    # Initialize the sequence with the first element as 1
    sequence = [1]
    # Initialize the score to 0
    score = 0
    # Loop through each quadruple
    for a, b, c, d in quadruples:
        # If the sequence is not long enough, extend it
        if len(sequence) < b:
            sequence.extend([x + 1 for x in range(len(sequence), b)])
        # If the sequence is long enough, but the last element is not greater than M, extend it
        if sequence[-1] < M:
            sequence.append(sequence[-1] + 1)
        # If the sequence is long enough and the last element is greater than M, extend it with the next possible value
        else:
            sequence.append(1)
        # If the difference between the elements at indices a and b is equal to c, add d to the score
        if sequence[b] - sequence[a] == c:
            score += d
    return score

def main():
    N, M, Q = map(int, input().split())
    quadruples = []
    for _ in range(Q):
        a, b, c, d = map(int, input().split())
        quadruples.append((a, b, c, d))
    print(get_maximum_score(N, M, Q, quadruples))

if __name__ == '__main__':
    main()

