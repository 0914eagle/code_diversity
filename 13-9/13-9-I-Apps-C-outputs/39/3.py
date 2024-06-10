
def get_expected_weight(n, m, likes, weights):
    # Initialize the expected weight vector
    expected_weight = [0] * n

    # Loop through each visit
    for i in range(m):
        # Randomly select a picture with probability proportional to its weight
        selected_picture = np.random.choice(n, p=weights / sum(weights))

        # Check if the selected picture is liked by Nauuo
        if likes[selected_picture]:
            # If liked, increase the weight by 1
            weights[selected_picture] += 1
        else:
            # If not liked, decrease the weight by 1
            weights[selected_picture] -= 1

        # Update the expected weight vector
        expected_weight[selected_picture] += weights[selected_picture]

    # Return the expected weight vector
    return expected_weight

def get_modular_expected_weight(n, m, likes, weights, modulo):
    # Get the expected weight vector
    expected_weight = get_expected_weight(n, m, likes, weights)

    # Create a list to store the final expected weight
    final_expected_weight = []

    # Loop through each picture
    for i in range(n):
        # Find the inverse of the weight modulo the modulo
        inverse_weight = modinv(weights[i], modulo)

        # Multiply the expected weight by the inverse weight and take the modulo
        final_expected_weight.append((expected_weight[i] * inverse_weight) % modulo)

    # Return the final expected weight vector
    return final_expected_weight

def modinv(a, m):
    # Extended Euclidean algorithm
    # Find the coefficients of the linear combination of a and m that equal 1
    # The modular multiplicative inverse is the coefficient of a
    # See https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Example
    s, t, r = a, m, a
    while r != 0:
        q = s // r
        s, t = t, s - q * t
        r, s = s, r - q * s
    if t < 0:
        t += m
    return t

if __name__ == '__main__':
    n, m = map(int, input().split())
    likes = list(map(int, input().split()))
    weights = list(map(int, input().split()))
    modulo = 998244353

    # Get the expected weight vector
    expected_weight = get_modular_expected_weight(n, m, likes, weights, modulo)

    # Print the expected weight vector
    print(*expected_weight, sep='\n')

