
def get_strengths(n, k, x, rangers):
    # Sort the rangers in increasing order of strength
    rangers.sort()
    
    # Perform the operation k times
    for i in range(k):
        # Take the bitwise XOR of the strength of each alternate ranger with x and update it's strength
        for j in range(0, n, 2):
            rangers[j] = rangers[j] ^ x
    
    # Return the maximum and minimum strength of the rangers after performing the operation k times
    return max(rangers), min(rangers)

def main():
    n, k, x = map(int, input().split())
    rangers = list(map(int, input().split()))
    print(*get_strengths(n, k, x, rangers))

if __name__ == '__main__':
    main()

