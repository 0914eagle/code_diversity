
def get_dominated_subarray(arr):
    # Initialize a dictionary to store the count of each number in the array
    count = {}
    for num in arr:
        if num not in count:
            count[num] = 1
        else:
            count[num] += 1
    
    # Find the number that occurs the most
    max_count = max(count.values())
    dominant_num = [num for num, count in count.items() if count == max_count][0]
    
    # Find the shortest subarray that contains the dominant number
    subarray_length = len(arr)
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == dominant_num and arr[j] == dominant_num:
                subarray_length = min(subarray_length, j-i+1)
    
    return subarray_length

def main():
    tests = int(input())
    for _ in range(tests):
        n = int(input())
        arr = list(map(int, input().split()))
        print(get_dominated_subarray(arr))

if __name__ == '__main__':
    main()

