
def get_tubes(tube_lengths, L1, L2):
    # sort the tube lengths in descending order
    tube_lengths.sort(reverse=True)
    
    # initialize the total length of air that can be avoided
    total_length = 0
    
    # loop through the tube lengths and find two pairs that fit the constraints
    for i in range(len(tube_lengths)):
        for j in range(i+1, len(tube_lengths)):
            if tube_lengths[i] + tube_lengths[j] <= L1 and tube_lengths[i+1] + tube_lengths[j+1] <= L2:
                total_length += tube_lengths[i] + tube_lengths[j] + tube_lengths[i+1] + tube_lengths[j+1]
                return total_length
    
    # if no pairs of tubes fit the constraints, return the string "Impossible"
    return "Impossible"

def main():
    L1, L2, N = map(int, input().split())
    tube_lengths = []
    for _ in range(N):
        tube_lengths.append(int(input()))
    print(get_tubes(tube_lengths, L1, L2))

if __name__ == '__main__':
    main()

