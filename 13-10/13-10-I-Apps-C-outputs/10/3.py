
def input_data():
    k, v = map(int, input().split())
    data = []
    for i in range(v):
        p, b = map(float, input().split())
        data.append((p, b))
    return k, v, data

def binary_voting(k, v, data):
    num_ballots = 0
    for p, b in data:
        num_ballots += p * b
    if k == 1:
        return num_ballots
    else:
        return binary_voting(k-1, v, data) + (num_ballots % 2) * 2**(k-1)

def find_max_expected_positions(k, v, data):
    max_expected_positions = 0
    for b in range(2**k):
        expected_positions = 0
        for p, b_i in data:
            if b & (2**(k-1)):
                expected_positions += p * (b_i % 2)
            else:
                expected_positions += p * (1 - b_i % 2)
        max_expected_positions = max(max_expected_positions, expected_positions)
    return max_expected_positions

def main():
    k, v, data = input_data()
    num_ballots = binary_voting(k, v, data)
    max_expected_positions = find_max_expected_positions(k, v, data)
    print(num_ballots)

if __name__ == '__main__':
    main()

