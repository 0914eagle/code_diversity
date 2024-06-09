
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
    for combination in combinations(lamps, k):
        # Check if the combination is valid
        if all(lamp[1] - lamp[0] >= k for lamp in combination):
            # Increment the answer
            answer += 1
    
    # Return the answer modulo 998244353
    return answer % 998244353

def main():
    # Read the input
    n, k = map(int, input().split())
    lamps = []
    for _ in range(n):
        l, r = map(int, input().split())
        lamps.append((l, r))
    
    # Call the get_answer function and print the result
    print(get_answer(n, k, lamps))

if __name__ == '__main__':
    main()

