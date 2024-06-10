
def get_expected_positions(probabilities, ballots):
    expected_positions = 0
    for i in range(len(probabilities)):
        expected_positions += probabilities[i] * ballots[i]
    return expected_positions

def get_best_ballots(probabilities, ballots, k):
    best_ballots = 0
    for i in range(1, 2**k):
        total_ballots = sum(ballots) + i
        expected_positions = get_expected_positions(probabilities, ballots) + i * (total_ballots % 2)
        if expected_positions > best_ballots:
            best_ballots = expected_positions
    return best_ballots

def main():
    k, v = map(int, input().split())
    probabilities = []
    ballots = []
    for i in range(v):
        probability, ballot = map(int, input().split())
        probabilities.append(probability)
        ballots.append(ballot)
    print(get_best_ballots(probabilities, ballots, k))

if __name__ == '__main__':
    main()

