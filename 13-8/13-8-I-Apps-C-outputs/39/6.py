
def get_rangers_strengths(n, k, x):
    # Sort the rangers in increasing order of their strengths
    rangers = sorted([int(input()) for _ in range(n)])
    
    # Perform the operation k times
    for _ in range(k):
        # Take the bitwise XOR of the strength of each alternate ranger with x and update it's strength
        for i in range(0, n, 2):
            rangers[i] ^= x
    
    # Return the maximum and minimum strength of the rangers after performing the operation k times
    return max(rangers), min(rangers)

def main():
    n, k, x = map(int, input().split())
    print(*get_rangers_strengths(n, k, x))

if __name__ == '__main__':
    main()

