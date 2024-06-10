
def get_tubes(tube_lengths, L1, L2):
    # Sort the tube lengths in descending order
    tube_lengths.sort(reverse=True)
    
    # Initialize the sum of the first two tube lengths and the sum of the last two tube lengths
    sum1 = 0
    sum2 = 0
    
    # Initialize the number of tubes used
    num_tubes = 0
    
    # Iterate through the tube lengths
    for i in range(len(tube_lengths)):
        # If the sum of the first two tube lengths is less than or equal to L1 and the sum of the last two tube lengths is less than or equal to L2, add the current tube length to the sum
        if sum1 + tube_lengths[i] <= L1 and sum2 + tube_lengths[i] <= L2:
            sum1 += tube_lengths[i]
            sum2 += tube_lengths[i]
            num_tubes += 1
        # If the sum of the first two tube lengths is greater than L1 and the sum of the last two tube lengths is less than or equal to L2, add the current tube length to the sum of the last two tube lengths
        elif sum1 > L1 and sum2 + tube_lengths[i] <= L2:
            sum2 += tube_lengths[i]
            num_tubes += 1
        # If the sum of the first two tube lengths is less than or equal to L1 and the sum of the last two tube lengths is greater than L2, add the current tube length to the sum of the first two tube lengths
        elif sum1 + tube_lengths[i] <= L1 and sum2 > L2:
            sum1 += tube_lengths[i]
            num_tubes += 1
        # If the sum of the first two tube lengths is greater than L1 and the sum of the last two tube lengths is greater than L2, break the loop
        else:
            break
    
    # If the number of tubes used is 4, return the sum of the four tubes
    if num_tubes == 4:
        return sum1 + sum2
    # If the number of tubes used is less than 4, return the word "Impossible"
    else:
        return "Impossible"

def main():
    L1, L2, N = map(int, input().split())
    tube_lengths = list(map(int, input().split()))
    print(get_tubes(tube_lengths, L1, L2))

if __name__ == '__main__':
    main()

