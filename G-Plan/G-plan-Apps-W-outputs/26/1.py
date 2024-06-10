
def smallest_exit_index(n, doors):
    left_ptr = 0
    right_ptr = 0
    left_open = 0
    right_open = 0
    min_index = float('inf')

    while right_ptr < n:
        if doors[right_ptr] == 0:
            left_open += 1
        else:
            right_open += 1

        while left_open > 0 and right_open > 0:
            if doors[left_ptr] == 0:
                left_open -= 1
            else:
                right_open -= 1
            left_ptr += 1

        if left_open == 0 or right_open == 0:
            min_index = min(min_index, right_ptr - left_ptr + 1)
        
        right_ptr += 1

    return min_index

if __name__ == "__main__":
    n = int(input())
    doors = list(map(int, input().split()))
    result = smallest_exit_index(n, doors)
    print(result)
