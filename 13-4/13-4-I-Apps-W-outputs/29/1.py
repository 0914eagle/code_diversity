
def get_longest_segment(arr):
    # Find the longest segment of consecutive equal integers
    current_segment = []
    longest_segment = []
    for i in range(len(arr)):
        if arr[i] not in current_segment:
            current_segment.append(arr[i])
        else:
            if len(current_segment) > len(longest_segment):
                longest_segment = current_segment
            current_segment = [arr[i]]
    if len(current_segment) > len(longest_segment):
        longest_segment = current_segment
    return longest_segment

def get_number_of_operations(arr):
    # Count the number of operations needed to remove all elements from the array
    number_of_operations = 0
    while len(arr) > 0:
        longest_segment = get_longest_segment(arr)
        arr = [x for x in arr if x not in longest_segment]
        number_of_operations += 1
    return number_of_operations

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(get_number_of_operations(arr))

