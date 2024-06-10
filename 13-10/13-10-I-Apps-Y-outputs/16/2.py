
def is_good_array(arr):
    if len(arr) % 6 != 0:
        return False
    
    count = [0] * 6
    for i in arr:
        count[i-4] += 1
    
    for i in range(6):
        if count[i] == 0:
            return False
    
    return True

def remove_min_elements(arr):
    if len(arr) == 0:
        return 0
    
    if is_good_array(arr):
        return 0
    
    min_element = 1000
    for i in range(len(arr)):
        if arr[i] < min_element:
            min_element = arr[i]
    
    count = 0
    for i in range(len(arr)):
        if arr[i] == min_element:
            count += 1
    
    return count + remove_min_elements(arr[1:])

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(remove_min_elements(arr))

