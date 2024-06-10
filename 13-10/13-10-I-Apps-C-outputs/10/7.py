
def input_data():
    k, v = map(int, input().split())
    probabilities = []
    ballots = []
    for _ in range(v - 1):
        probability, ballot = map(int, input().split())
        probabilities.append(probability)
        ballots.append(ballot)
    return k, v, probabilities, ballots

def expected_positions_yraglac(k, v, probabilities, ballots):
    expected_positions = 0
    for i in range(v):
        probability = probabilities[i]
        ballot = ballots[i]
        if probability == 0:
            continue
        expected_positions += probability * (ballot % 2)
    return expected_positions

def maximize_expected_positions_yraglac(k, v, probabilities, ballots):
    max_expected_positions = -1
    max_ballots = 0
    for ballots_cast in range(2**k):
        expected_positions = expected_positions_yraglac(k, v, probabilities, ballots_cast)
        if expected_positions > max_expected_positions:
            max_expected_positions = expected_positions
            max_ballots = ballots_cast
    return max_ballots

def main():
    k, v, probabilities, ballots = input_data()
    print(maximize_expected_positions_yraglac(k, v, probabilities, ballots))

if __name__ == '__main__':
    main()

