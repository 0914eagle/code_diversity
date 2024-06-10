
def get_min_chairs(n, left_counts, right_counts):
    # Initialize the minimum number of chairs to be the sum of all left and right counts
    min_chairs = sum(left_counts) + sum(right_counts)
    
    # Iterate over the guests and check if they can be seated in a single circle
    for i in range(n):
        # Check if the guest has enough left and right chairs to be seated in a single circle
        if left_counts[i] + right_counts[i] <= min_chairs:
            # If the guest can be seated in a single circle, remove their left and right counts from the minimum number of chairs
            min_chairs -= left_counts[i] + right_counts[i]
    
    return min_chairs

def main():
    n = int(input())
    left_counts = []
    right_counts = []
    
    # Read the input
    for i in range(n):
        left_count, right_count = map(int, input().split())
        left_counts.append(left_count)
        right_counts.append(right_count)
    
    # Call the function to get the minimum number of chairs
    min_chairs = get_min_chairs(n, left_counts, right_counts)
    
    # Print the result
    print(min_chairs)

if __name__ == '__main__':
    main()

