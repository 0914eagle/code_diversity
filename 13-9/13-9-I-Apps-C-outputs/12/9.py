
def get_maximum_sum(arr):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the maximum sum and the number of positive elements
    max_sum = 0
    pos_count = 0
    # Iterate through the array and calculate the maximum sum
    for i in range(len(arr)):
        if arr[i] > 0:
            pos_count += 1
        if pos_count > (len(arr) + 1) // 2:
            break
        max_sum += arr[i]
    return max_sum

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(get_maximum_sum(arr))

if __name__ == '__main__':
    main()

