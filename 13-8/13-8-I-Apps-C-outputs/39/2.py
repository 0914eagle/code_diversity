
def get_strengths(n, k, x):
    # Sort the rangers in increasing order of strength
    rangers = sorted([int(input()) for _ in range(n)])
    
    # Perform the operation k times
    for _ in range(k):
        for i in range(0, n, 2):
            # XOR the strength of each alternate ranger with x and update it
            rangers[i] = rangers[i] ^ x
    
    # Return the maximum and minimum strengths of the rangers
    return max(rangers), min(rangers)

def main():
    n, k, x = map(int, input().split())
    print(*get_strengths(n, k, x))

if __name__ == '__main__':
    main()

