
def get_min_steps(n, b):
    # Initialize the minimum number of steps as 0
    min_steps = 0
    
    # Initialize the current array as all zeros
    current_array = [0] * n
    
    # Loop through each element in the target array
    for i in range(n):
        # If the current element is not equal to the target element, we need to take action
        if current_array[i] != b[i]:
            # Calculate the difference between the current element and the target element
            diff = b[i] - current_array[i]
            
            # If the difference is positive, we need to add 1 to the current element and all subsequent elements
            if diff > 0:
                current_array[i] += 1
                for j in range(i+1, n):
                    current_array[j] += 1
                    
            # If the difference is negative, we need to subtract 1 from the current element and all subsequent elements
            elif diff < 0:
                current_array[i] -= 1
                for j in range(i+1, n):
                    current_array[j] -= 1
                    
            # Increment the minimum number of steps
            min_steps += 1
    
    # Return the minimum number of steps
    return min_steps

def main():
    n = int(input())
    b = list(map(int, input().split()))
    print(get_min_steps(n, b))

if __name__ == '__main__':
    main()

