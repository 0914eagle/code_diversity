
def get_min_matches(n):
    # Initialize the minimum number of matches to buy as n
    min_matches = n
    # Iterate from 1 to n
    for i in range(1, n + 1):
        # Check if n - i is a valid number
        if n - i > 0:
            # Check if n - i is a valid number
            if (n - i) % 2 == 0:
                # Update the minimum number of matches to buy
                min_matches = min(min_matches, i + (n - i) // 2)
    # Return the minimum number of matches to buy
    return min_matches

def main():
    q = int(input())
    for _ in range(q):
        n = int(input())
        print(get_min_matches(n))

if __name__ == '__main__':
    main()

