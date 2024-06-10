
def get_probabilities(N):
    probabilities = []
    for _ in range(N):
        password, probability = input().split()
        probabilities.append((password, float(probability)))
    return probabilities

def get_optimal_order(probabilities):
    # Sort the probabilities in descending order based on the probability of the password being correct
    probabilities.sort(key=lambda x: x[1], reverse=True)
    return probabilities

def get_expected_number_of_attempts(probabilities):
    # Calculate the expected number of attempts to find the correct password using the optimal order
    expected_number_of_attempts = 0
    for password, probability in probabilities:
        expected_number_of_attempts += probability
    return expected_number_of_attempts

if __name__ == '__main__':
    N = int(input())
    probabilities = get_probabilities(N)
    optimal_order = get_optimal_order(probabilities)
    expected_number_of_attempts = get_expected_number_of_attempts(optimal_order)
    print(expected_number_of_attempts)

