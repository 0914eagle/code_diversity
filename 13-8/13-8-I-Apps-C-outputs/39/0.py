
def get_max_and_min_strengths(strengths, x, k):
    # Sort the strengths in increasing order
    strengths.sort()
    
    # Perform the operation k times
    for _ in range(k):
        # Take the bitwise XOR of each alternate strength with x and update it
        for i in range(0, len(strengths), 2):
            strengths[i] ^= x
    
    # Return the maximum and minimum strengths after the operation
    return max(strengths), min(strengths)

def main():
    n, k, x = map(int, input().split())
    strengths = list(map(int, input().split()))
    print(*get_max_and_min_strengths(strengths, x, k))

if __name__ == '__main__':
    main()

