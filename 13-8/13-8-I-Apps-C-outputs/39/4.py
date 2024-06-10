
def get_strengths(n, k, x, rangers):
    # Sort the rangers in increasing order of strength
    rangers.sort()
    
    # Perform the operation k times
    for _ in range(k):
        # Take the bitwise XOR of the strength of each alternate ranger with x and update it's strength
        for i in range(0, n, 2):
            rangers[i] = rangers[i] ^ x
    
    # Return the minimum and maximum strength of the rangers after performing the operation k times
    return min(rangers), max(rangers)

def main():
    n, k, x = map(int, input().split())
    rangers = list(map(int, input().split()))
    print(*get_strengths(n, k, x, rangers))

if __name__ == '__main__':
    main()

