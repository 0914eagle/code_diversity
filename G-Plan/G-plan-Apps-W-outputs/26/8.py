
def smallest_index_to_exit(n, doors):
    left_opened = 0
    right_opened = 0
    left_pointer = 0
    right_pointer = 0
    min_index = float('inf')

    while right_pointer < n:
        if doors[right_pointer] == 0:
            left_opened += 1
        else:
            right_opened += 1

        while left_opened > 0 and right_opened > 0:
            if doors[left_pointer] == 0:
                left_opened -= 1
            else:
                right_opened -= 1
            left_pointer += 1

        if left_opened == 0 or right_opened == 0:
            min_index = min(min_index, right_pointer - left_pointer + 1)

        right_pointer += 1

    return min_index

if __name__ == "__main__":
    n = int(input())
    doors = list(map(int, input().split()))
    result = smallest_index_to_exit(n, doors)
    print(result)
