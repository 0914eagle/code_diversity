
def get_max_sum(arr):
    # Find the maximum element in the array
    max_element = max(arr)
    # Initialize the maximum sum to the maximum element
    max_sum = max_element
    # Loop through the array and find the maximum sum by changing the sign of the elements
    for i in range(len(arr)):
        current_sum = 0
        for j in range(len(arr)):
            if j != i:
                current_sum += arr[j]
        max_sum = max(max_sum, current_sum)
    return max_sum

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(get_max_sum(arr))

if __name__ == '__main__':
    main()

