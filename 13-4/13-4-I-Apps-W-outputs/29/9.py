
def get_longest_segment(arr):
    # Find the longest segment of consecutive equal integers
    current_seg = []
    longest_seg = []
    for i in range(len(arr)):
        if arr[i] not in current_seg:
            current_seg.append(arr[i])
        if len(current_seg) > len(longest_seg):
            longest_seg = current_seg
        if i == len(arr) - 1 and len(current_seg) > len(longest_seg):
            longest_seg = current_seg
    return longest_seg

def remove_segment(arr, segment):
    # Remove the segment from the array
    return [x for x in arr if x not in segment]

def count_operations(arr):
    # Count the number of operations needed to remove all elements from the array
    count = 0
    while len(arr) > 0:
        segment = get_longest_segment(arr)
        arr = remove_segment(arr, segment)
        count += 1
    return count

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(count_operations(arr))

if __name__ == '__main__':
    main()

