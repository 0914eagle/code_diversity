
import math

def get_expected_weights(n, m, likes, weights):
    # Initialize the expected weights
    expected_weights = [0] * n

    # Loop through each visit
    for visit in range(m):
        # Choose a picture with probability proportional to its weight
        picture_index = choose_picture(weights)

        # If the picture is liked, increase its weight by 1
        if likes[picture_index] == 1:
            weights[picture_index] += 1
        # Otherwise, decrease its weight by 1
        else:
            weights[picture_index] -= 1

        # Update the expected weight
        expected_weights[picture_index] += weights[picture_index]

    # Return the expected weights modulo 998244353
    return [get_modulo_998244353(weight) for weight in expected_weights]

def choose_picture(weights):
    # Calculate the sum of all weights
    total_weight = sum(weights)

    # Choose a picture with probability proportional to its weight
    random_number = random.randint(1, total_weight)
    current_weight = 0
    for i in range(len(weights)):
        current_weight += weights[i]
        if random_number <= current_weight:
            return i

def get_modulo_998244353(number):
    return number % 998244353

if __name__ == '__main__':
    n, m = map(int, input().split())
    likes = list(map(int, input().split()))
    weights = list(map(int, input().split()))
    print(*get_expected_weights(n, m, likes, weights), sep='\n')

