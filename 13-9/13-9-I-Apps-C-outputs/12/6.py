
def get_maximum_sum(array):
    # Sort the array in non-decreasing order
    array.sort()
    # Initialize the maximum sum and the number of elements to change
    max_sum = 0
    num_elements = len(array) // 2
    # Loop through the array and calculate the maximum sum
    for i in range(num_elements):
        max_sum += array[i] + array[~i]
    return max_sum

def main():
    # Read the input array
    n = int(input())
    array = list(map(int, input().split()))
    # Call the get_maximum_sum function and print the result
    print(get_maximum_sum(array))

if __name__ == '__main__':
    main()

