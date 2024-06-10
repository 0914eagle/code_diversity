
def get_sum(arr):
    return sum(arr)

def can_divide(arr):
    n = len(arr)
    if n == 1:
        return True
    if n == 2:
        return arr[0] == arr[1]
    if arr[0] == arr[1]:
        return can_divide(arr[1:])
    if arr[-1] == arr[-2]:
        return can_divide(arr[:-1])
    return False

def move_element(arr, index, new_index):
    element = arr[index]
    arr.pop(index)
    arr.insert(new_index, element)
    return arr

def can_divide_after_moving(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if can_divide(move_element(arr, i, j)):
                return True
    return False

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    if can_divide_after_moving(arr):
        print("YES")
    else:
        print("NO")

