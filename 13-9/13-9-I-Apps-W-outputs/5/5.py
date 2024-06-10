
def get_combinations(n, k):
    # Calculate the binomial coefficient (n choose k)
    result = 1
    for i in range(k):
        result = result * (n - i) / (i + 1)
    return result

def get_answer(n, k, lamps):
    # Initialize the answer to 0
    answer = 0

    # Iterate over all possible combinations of k lamps
    for combination in itertools.combinations(lamps, k):
        # Check if all lamps in the combination are turned on at the same time
        if all(lamp[0] <= lamp[1] for lamp in combination):
            # Increment the answer
            answer += 1

    # Return the answer modulo 998244353
    return answer % 998244353

def main():
    # Read the input
    n, k = map(int, input().split())
    lamps = []
    for _ in range(n):
        lamps.append(tuple(map(int, input().split())))

    # Call the get_answer function and print the result
    print(get_answer(n, k, lamps))

if __name__ == '__main__':
    main()

