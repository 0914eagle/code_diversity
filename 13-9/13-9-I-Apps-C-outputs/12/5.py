
def get_maximum_sum(arr):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the maximum sum and the number of elements to be changed
    max_sum = 0
    n = len(arr) // 2
    # Loop through the array and find the maximum sum
    for i in range(n):
        max_sum += arr[i] + arr[n + i]
    return max_sum

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(get_maximum_sum(arr))

if __name__ == '__main__':
    main()

