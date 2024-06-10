
def get_ranger_strengths(n, k, x, ranger_strengths):
    # Sort the ranger strengths in increasing order
    sorted_ranger_strengths = sorted(ranger_strengths)

    # Initialize the minimum and maximum strengths
    min_strength, max_strength = sorted_ranger_strengths[0], sorted_ranger_strengths[-1]

    # Perform the operation k times
    for i in range(k):
        # Take the bitwise XOR of the strength of each alternate ranger with x and update its strength
        for j in range(0, n, 2):
            sorted_ranger_strengths[j] = sorted_ranger_strengths[j] ^ x

        # Update the minimum and maximum strengths
        min_strength = min(min_strength, sorted_ranger_strengths[0])
        max_strength = max(max_strength, sorted_ranger_strengths[-1])

    return min_strength, max_strength

def main():
    n, k, x = map(int, input().split())
    ranger_strengths = list(map(int, input().split()))
    min_strength, max_strength = get_ranger_strengths(n, k, x, ranger_strengths)
    print(min_strength, max_strength)

if __name__ == '__main__':
    main()

