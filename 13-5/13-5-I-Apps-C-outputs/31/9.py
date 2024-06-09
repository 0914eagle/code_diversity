
def get_max_earnings(a):
    # Initialize the maximum earnings to 0
    max_earnings = 0
    # Loop through each gemstone
    for i in range(len(a)):
        # Check if the gemstone is not smashed
        if a[i] > 0:
            # Find the largest multiple of the current gemstone that is less than or equal to the length of the array
            multiple = (i // a[i]) * a[i]
            # Check if the multiple is not the current gemstone
            if multiple != i:
                # Add the earnings from smashing the current gemstone to the maximum earnings
                max_earnings += a[i]
                # Set the earnings of the multiple to 0
                a[multiple] = 0
    # Return the maximum earnings
    return max_earnings

def main():
    # Read the number of gemstones and their earnings from stdin
    n = int(input())
    a = list(map(int, input().split()))
    # Call the function to get the maximum earnings
    max_earnings = get_max_earnings(a)
    # Print the maximum earnings
    print(max_earnings)

if __name__ == '__main__':
    main()

