
def smallest_exit_index(n, doors):
    left_pointer = 0
    right_pointer = 0
    left_open = 0
    right_open = 0
    min_index = float('inf')

    while right_pointer < n:
        if doors[right_pointer] == 0:
            left_open += 1
        else:
            right_open += 1

        while left_open > 0 and right_open > 0:
            if doors[left_pointer] == 0:
                left_open -= 1
            else:
                right_open -= 1
            left_pointer += 1

        if left_open == 0 or right_open == 0:
            min_index = min(min_index, right_pointer - left_pointer + 1)

        right_pointer += 1

    return min_index

if __name__ == "__main__":
    n = int(input())
    doors = list(map(int, input().split()))
    result = smallest_exit_index(n, doors)
    print(result)
