
def get_max_earned(a):
    # Initialize the maximum amount of money to be earned
    max_earned = 0
    # Loop through each gemstone
    for i in range(len(a)):
        # Check if the gemstone is not smashed
        if a[i] > 0:
            # Get the current amount of money earned
            current_earned = a[i]
            # Loop through each gemstone after the current gemstone
            for j in range(i+1, len(a)):
                # Check if the gemstone is not smashed and is a multiple of the current gemstone
                if a[j] > 0 and j % i == 0:
                    # Smash the gemstone and add its value to the current amount of money earned
                    current_earned += a[j]
                    # Mark the gemstone as smashed
                    a[j] = 0
            # Update the maximum amount of money earned if the current amount is greater
            max_earned = max(max_earned, current_earned)
    return max_earned

def main():
    # Read the number of gemstones and their values from stdin
    n = int(input())
    a = list(map(int, input().split()))
    # Get the maximum amount of money that can be earned
    max_earned = get_max_earned(a)
    # Print the maximum amount of money earned
    print(max_earned)

if __name__ == '__main__':
    main()

