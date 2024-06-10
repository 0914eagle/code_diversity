
def get_expected_weights(n, m, a, w):
    # Initialize the expected weights as an array of zeros
    expected_weights = [0] * n

    # Loop through each visit
    for i in range(m):
        # Generate a random number between 1 and n
        random_picture = random.randint(1, n)

        # If the random picture is liked by Nauuo
        if a[random_picture - 1] == 1:
            # Increase the weight of the picture by 1
            expected_weights[random_picture - 1] += 1
        else:
            # Decrease the weight of the picture by 1
            expected_weights[random_picture - 1] -= 1

    # Loop through each picture
    for i in range(n):
        # Find the gcd of the expected weight and 998244353
        gcd = math.gcd(expected_weights[i], 998244353)

        # Calculate the modular inverse of the gcd
        mod_inv = pow(gcd, -1, 998244353)

        # Calculate the expected weight modulo 998244353
        expected_weights[i] = (expected_weights[i] * mod_inv) % 998244353

    return expected_weights

def main():
    # Read the input data
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    w = list(map(int, input().split()))

    # Calculate the expected weights
    expected_weights = get_expected_weights(n, m, a, w)

    # Print the expected weights
    for weight in expected_weights:
        print(weight)

if __name__ == '__main__':
    main()

