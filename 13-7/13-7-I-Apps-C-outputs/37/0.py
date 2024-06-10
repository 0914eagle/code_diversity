
def get_tubes(tube_lengths, L1, L2):
    # Sort the tube lengths in descending order
    tube_lengths.sort(reverse=True)
    
    # Initialize the total length of the tubes as 0
    total_length = 0
    
    # Loop through the tube lengths and find two pairs of tubes that add up to L1 and L2
    for i in range(len(tube_lengths)):
        for j in range(i+1, len(tube_lengths)):
            if tube_lengths[i] + tube_lengths[j] <= L1 and tube_lengths[i] + tube_lengths[j] <= L2:
                total_length += tube_lengths[i] + tube_lengths[j]
                break
    
    return total_length

def main():
    L1, L2, N = map(int, input().split())
    tube_lengths = []
    for _ in range(N):
        tube_lengths.append(int(input()))
    
    print(get_tubes(tube_lengths, L1, L2))

if __name__ == '__main__':
    main()

