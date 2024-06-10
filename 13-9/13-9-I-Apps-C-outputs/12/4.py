
def get_max_sum(arr):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the maximum sum and the number of elements to be changed
    max_sum = 0
    num_elements = len(arr) // 2
    # Loop through the array and calculate the maximum sum
    for i in range(num_elements):
        max_sum += arr[i] + arr[num_elements + i]
    return max_sum

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(get_max_sum(arr))

if __name__ == '__main__':
    main()

