
def get_min_snacks(a, b):
    # Find the smaller number between a and b
    smaller = min(a, b)
    # Find the larger number between a and b
    larger = max(a, b)
    # Initialize the minimum number of snacks to be the smaller number
    min_snacks = smaller
    # Loop through all possible numbers of snacks from smaller to larger
    for i in range(smaller, larger + 1):
        # Check if the number of snacks is divisible by both a and b
        if i % a == 0 and i % b == 0:
            # If it is, update the minimum number of snacks
            min_snacks = i
            break
    return min_snacks

def main():
    a, b = map(int, input().split())
    print(get_min_snacks(a, b))

if __name__ == '__main__':
    main()

