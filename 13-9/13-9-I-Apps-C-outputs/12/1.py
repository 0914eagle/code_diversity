
def get_max_sum(arr):
    # Find the maximum element in the array
    max_element = max(arr)
    
    # Initialize the maximum sum to be the sum of the maximum element
    max_sum = max_element
    
    # Iterate through the array and find the maximum sum by changing the sign of the elements
    for i in range(len(arr)):
        current_sum = 0
        for j in range(len(arr)):
            if i == j:
                current_sum += arr[j]
            else:
                current_sum += arr[j] * (-1)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(get_max_sum(arr))

if __name__ == '__main__':
    main()

