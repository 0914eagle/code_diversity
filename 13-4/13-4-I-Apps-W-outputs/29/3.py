
def get_longest_segment(arr):
    # find the longest segment of consecutive equal integers
    longest_segment = []
    for i in range(len(arr)):
        if arr[i] not in longest_segment:
            longest_segment.append(arr[i])
        else:
            break
    return longest_segment

def remove_segment(arr, segment):
    # remove the segment from the array
    return [x for x in arr if x not in segment]

def get_number_of_operations(arr):
    # compute the number of operations needed to remove all elements from the array
    number_of_operations = 0
    while len(arr) > 0:
        longest_segment = get_longest_segment(arr)
        arr = remove_segment(arr, longest_segment)
        number_of_operations += 1
    return number_of_operations

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(get_number_of_operations(arr))

