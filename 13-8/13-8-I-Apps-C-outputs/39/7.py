
def get_rangers_strength(n, k, x, rangers):
    # Sort the rangers in increasing order of their strength
    rangers.sort()
    
    # Perform the operation k times
    for _ in range(k):
        # Take the bitwise XOR of the strength of each alternate ranger with x and update it's strength
        for i in range(0, len(rangers), 2):
            rangers[i] = rangers[i] ^ x
    
    # Return the maximum and minimum strength of the rangers after performing the operation k times
    return max(rangers), min(rangers)

def main():
    n, k, x = map(int, input().split())
    rangers = list(map(int, input().split()))
    print(*get_rangers_strength(n, k, x, rangers))

if __name__ == '__main__':
    main()

