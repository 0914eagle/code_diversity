
def get_max_earnings(a):
    # Initialize variables
    n = len(a)
    smashed = [False] * n
    earnings = 0
    
    # Iterate through the gems
    for i in range(n):
        # If the gem is not smashed and its value is positive, smash it
        if not smashed[i] and a[i] > 0:
            smashed[i] = True
            earnings += a[i]
    
    # Return the maximum earnings
    return earnings

def main():
    # Read the input
    n = int(input())
    a = list(map(int, input().split()))
    
    # Call the function to get the maximum earnings
    max_earnings = get_max_earnings(a)
    
    # Print the result
    print(max_earnings)

if __name__ == '__main__':
    main()

