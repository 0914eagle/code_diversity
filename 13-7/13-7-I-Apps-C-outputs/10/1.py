
def get_candy_values(a_values, b_values):
    # Initialize the sum of candy values for each sibling
    alf_sum = 0
    beata_sum = 0
    
    # Iterate through the candy values
    for i in range(len(a_values)):
        # Add the candy value to the corresponding sibling's sum
        alf_sum += a_values[i]
        beata_sum += b_values[i]
    
    # Find the difference between the two siblings' sums
    diff = abs(alf_sum - beata_sum)
    
    # Initialize the output string
    output = ""
    
    # Iterate through the candy values again
    for i in range(len(a_values)):
        # If the difference is 0, all candy values are equal
        if diff == 0:
            # Add the candy value to both siblings' output strings
            output += "AB"[i % 2]
        # If the difference is not 0, choose the sibling with the lower sum
        else:
            # Add the candy value to the sibling with the lower sum
            if alf_sum < beata_sum:
                output += "A"
                alf_sum += a_values[i]
            else:
                output += "B"
                beata_sum += b_values[i]
    
    # Return the output string
    return output

def main():
    # Read the input
    N = int(input())
    a_values = list(map(int, input().split()))
    b_values = list(map(int, input().split()))
    
    # Call the function to get the candy values
    output = get_candy_values(a_values, b_values)
    
    # Print the output
    print(output)

if __name__ == '__main__':
    main()

