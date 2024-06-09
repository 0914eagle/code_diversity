
def get_min_matches(n):
    # Initialize the minimum number of matches to buy as n
    min_matches = n
    # Loop through all possible values of a and b
    for a in range(1, n):
        for b in range(1, n):
            # Check if a + b = c is a correct match equation
            if a + b == n:
                # If it is, update the minimum number of matches to buy
                min_matches = min(min_matches, a + b)
    return min_matches

def main():
    q = int(input())
    for _ in range(q):
        n = int(input())
        print(get_min_matches(n))

if __name__ == '__main__':
    main()

