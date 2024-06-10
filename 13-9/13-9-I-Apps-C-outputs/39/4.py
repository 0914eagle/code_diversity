
def get_expected_weights(n, m, likes, weights):
    # Initialize the expected weights
    expected_weights = [0] * n

    # Loop through each visit
    for visit in range(m):
        # Choose a picture randomly based on their weights
        picture = choose_picture(weights)

        # If Nauuo likes the picture, increase its weight by 1
        if likes[picture]:
            weights[picture] += 1
        # Otherwise, decrease its weight by 1
        else:
            weights[picture] -= 1

        # Calculate the expected weight of the picture
        expected_weights[picture] += weights[picture] / m

    return expected_weights

def choose_picture(weights):
    # Normalize the weights to get probabilities
    probabilities = [weight / sum(weights) for weight in weights]

    # Choose a picture based on its probability
    picture = np.random.choice(len(weights), p=probabilities)

    return picture

def main():
    n, m = map(int, input().split())
    likes = list(map(int, input().split()))
    weights = list(map(int, input().split()))

    expected_weights = get_expected_weights(n, m, likes, weights)

    print(*expected_weights)

if __name__ == '__main__':
    main()

