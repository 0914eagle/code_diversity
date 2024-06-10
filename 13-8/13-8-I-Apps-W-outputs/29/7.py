
def get_max_birds(ell, d, n, positions):
    # Sort the positions of the birds
    positions.sort()
    
    # Initialize the number of birds that can sit
    max_birds = 0
    
    # Iterate through the positions of the birds
    for i in range(n):
        # Check if the current bird is within the allowed distance from the pole
        if positions[i] >= d and positions[i] <= ell - d:
            # Check if the current bird is within the allowed distance from the previous bird
            if i == 0 or positions[i] - positions[i-1] >= d:
                max_birds += 1
    
    return max_birds

def main():
    ell, d, n = map(int, input().split())
    positions = []
    for i in range(n):
        positions.append(int(input()))
    print(get_max_birds(ell, d, n, positions))

if __name__ == '__main__':
    main()

