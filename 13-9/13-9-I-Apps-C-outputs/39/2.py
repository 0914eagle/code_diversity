
def get_expected_weights(n, m, likes, weights):
    # Initialize the expected weights
    expected_weights = [0] * n

    # Iterate over each visit
    for visit in range(m):
        # Randomly select a picture with probability proportional to its weight
        selected_picture = np.random.choice(n, p=weights / sum(weights))

        # Check if the selected picture is liked by Nauuo
        if likes[selected_picture]:
            # Add 1 to the expected weight if the picture is liked
            expected_weights[selected_picture] += 1
        else:
            # Subtract 1 from the expected weight if the picture is not liked
            expected_weights[selected_picture] -= 1

    # Return the expected weights modulo 998244353
    return [expected_weight % 998244353 for expected_weight in expected_weights]

def main():
    # Read the input
    n, m = map(int, input().split())
    likes = list(map(int, input().split()))
    weights = list(map(int, input().split()))

    # Calculate the expected weights
    expected_weights = get_expected_weights(n, m, likes, weights)

    # Print the expected weights
    print(*expected_weights, sep='\n')

if __name__ == '__main__':
    main()

