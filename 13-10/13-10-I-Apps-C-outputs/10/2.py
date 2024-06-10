
def get_ballots(k, v, probs, ballots):
    # Calculate the expected number of positions held by Yraglac for each number of ballots
    expected_positions = []
    for b in range(2**k):
        num_positions = 0
        for i in range(v):
            if ballots[i] & b:
                num_positions += 1
        expected_positions.append(num_positions)
    
    # Return the number of ballots that maximizes the expected number of positions held by Yraglac
    return expected_positions.index(max(expected_positions))

def main():
    k, v = map(int, input().split())
    probs = []
    ballots = []
    for i in range(v):
        prob, ballot = map(int, input().split())
        probs.append(prob)
        ballots.append(ballot)
    print(get_ballots(k, v, probs, ballots))

if __name__ == '__main__':
    main()

