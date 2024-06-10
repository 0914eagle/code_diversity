
def calculate_expected_weights(n, m, a, w):
    # Initialize the expected weights as zero
    expected_weights = [0] * n

    # Loop through each visit
    for i in range(m):
        # Choose a picture uniformly at random
        picture_index = random.randint(0, n - 1)

        # If the picture is liked, increase its weight by 1
        if a[picture_index] == 1:
            expected_weights[picture_index] += 1
        # Otherwise, decrease its weight by 1
        else:
            expected_weights[picture_index] -= 1

    # Calculate the final expected weights modulo 998244353
    final_expected_weights = [0] * n
    for i in range(n):
        final_expected_weights[i] = expected_weights[i] % 998244353

    return final_expected_weights

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    w = list(map(int, input().split()))
    expected_weights = calculate_expected_weights(n, m, a, w)
    print(*expected_weights, sep='\n')

if __name__ == '__main__':
    main()

