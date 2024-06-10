
def get_max_min_strength(n, k, x, strengths):
    # Sort the strengths in ascending order
    sorted_strengths = sorted(strengths)

    # Perform the operation k times
    for i in range(k):
        for j in range(0, len(sorted_strengths), 2):
            # Update the strength of each alternate ranger
            sorted_strengths[j] = sorted_strengths[j] ^ x

    # Return the maximum and minimum strengths after the operation
    return max(sorted_strengths), min(sorted_strengths)

def main():
    n, k, x = map(int, input().split())
    strengths = list(map(int, input().split()))
    print(*get_max_min_strength(n, k, x, strengths))

if __name__ == '__main__':
    main()

