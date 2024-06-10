
def read_input():
    k, v = map(int, input().split())
    probabilities = []
    ballots = []
    for i in range(v - 1):
        probability, ballot = map(int, input().split())
        probabilities.append(probability)
        ballots.append(ballot)
    return k, v, probabilities, ballots

def expected_positions(k, v, probabilities, ballots):
    total_ballots = sum(ballot * probability for ballot, probability in zip(ballots, probabilities))
    total_ballots_binary = format(total_ballots, 'b')
    yraglac_positions = sum(int(bit) for bit in total_ballots_binary[-k:])
    return yraglac_positions

def maximize_yraglac_positions(k, v, probabilities, ballots):
    max_yraglac_positions = -1
    max_ballots = 0
    for ballots in range(2**k):
        yraglac_positions = expected_positions(k, v, probabilities, ballots)
        if yraglac_positions > max_yraglac_positions:
            max_yraglac_positions = yraglac_positions
            max_ballots = ballots
    return max_ballots

def main():
    k, v, probabilities, ballots = read_input()
    print(maximize_yraglac_positions(k, v, probabilities, ballots))

if __name__ == '__main__':
    main()

