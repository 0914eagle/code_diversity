
def count_arrays(n, m):
    # Initialize a list to store the arrays
    arrays = []
    
    # Loop through all possible values of the first element
    for i in range(1, m + 1):
        # Add the first element to the array
        array = [i]
        
        # Loop through the remaining elements
        for j in range(1, n):
            # Find the next element that is not equal to any of the previous elements
            element = 1
            while element in array:
                element += 1
            if element > m:
                break
            
            # Add the element to the array
            array.append(element)
            
            # Check if the array is strictly ascending before the i-th element and strictly descending after it
            if array[j] < array[j - 1] and array[j] > array[j + 1]:
                # Add the array to the list of arrays
                arrays.append(array)
                break
    
    # Return the number of arrays modulo 998244353
    return len(arrays) % 998244353

def main():
    n, m = map(int, input().split())
    print(count_arrays(n, m))

if __name__ == '__main__':
    main()

