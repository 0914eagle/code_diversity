
def can_reduce_to_one(arr):
    # Check if all elements in the array are the same
    if len(set(arr)) == 1:
        return True
    
    # Sort the array in ascending order
    arr.sort()
    
    # Initialize a variable to keep track of the minimum number of elements needed to reach the target
    min_elements = 1
    
    # Iterate over the array
    for i in range(len(arr)):
        # Check if the current element is within the target range
        if arr[i] >= min_elements:
            # Update the minimum number of elements needed to reach the target
            min_elements = arr[i]
        else:
            # If the current element is not within the target range, return False
            return False
    
    # If all elements are within the target range, return True
    return True

def main():
    # Read the number of test cases
    t = int(input())
    
    # Iterate over the test cases
    for _ in range(t):
        # Read the length of the array
        n = int(input())
        
        # Read the array
        arr = list(map(int, input().split()))
        
        # Check if it is possible to reduce the array to one element
        if can_reduce_to_one(arr):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()

