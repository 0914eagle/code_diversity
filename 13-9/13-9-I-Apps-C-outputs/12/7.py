
def get_max_sum(arr):
    # Find the maximum element in the array
    max_element = max(arr)
    # Initialize the maximum sum to be the sum of all elements
    max_sum = sum(arr)
    # Loop through each element in the array
    for i in range(len(arr)):
        # If the current element is not the maximum element, flip its sign
        if arr[i] != max_element:
            arr[i] = -arr[i]
        # Calculate the sum of the array after flipping the sign
        sum_after_flip = sum(arr)
        # If the sum after flipping the sign is greater than the current maximum sum, update the maximum sum
        if sum_after_flip > max_sum:
            max_sum = sum_after_flip
        # Flip the sign back to its original value
        arr[i] = -arr[i]
    return max_sum

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(get_max_sum(arr))

if __name__ == '__main__':
    main()

