
def calculate_expected_score(n, k):
    # Initialize a list to store the expected score for each side
    expected_score = [0] * (n + 1)
    
    # Base case: if we can only roll the die once, the expected score is the sum of all sides
    if k == 1:
        return sum(range(1, n + 1))
    
    # Recursive case: calculate the expected score for each side
    for i in range(1, n + 1):
        # Roll the die and calculate the expected score for each side
        expected_score[i] = (i / n) + (k - 1) * calculate_expected_score(n, k - 1)
    
    # Return the maximum expected score
    return max(expected_score)

def main():
    n, k = map(int, input().split())
    print(calculate_expected_score(n, k))

if __name__ == '__main__':
    main()

