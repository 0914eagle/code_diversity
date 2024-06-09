
def get_min_matches(n):
    # Initialize the minimum number of matches to buy as n
    min_matches = n
    # Iterate through the possible values of a and b
    for a in range(1, n):
        for b in range(a, n):
            # Check if a + b = c is a correct match equation
            c = a + b
            if a > 0 and b > 0 and c > 0:
                # If it is, update the minimum number of matches to buy
                min_matches = min(min_matches, a + b - n)
    return min_matches

def main():
    q = int(input())
    for _ in range(q):
        n = int(input())
        print(get_min_matches(n))

if __name__ == '__main__':
    main()

