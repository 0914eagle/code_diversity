
def get_good_array(arr):
    n = len(arr)
    if n % 6 != 0:
        return -1
    
    count = [0, 0, 0, 0, 0, 0]
    for i in range(n):
        count[arr[i] - 4] += 1
    
    if count[0] != count[1] or count[2] != count[3] or count[4] != count[5]:
        return -1
    
    return 0

def remove_elements(arr):
    n = len(arr)
    if n == 0:
        return 0
    
    count = [0, 0, 0, 0, 0, 0]
    for i in range(n):
        count[arr[i] - 4] += 1
    
    min_remove = 0
    for i in range(6):
        if count[i] > 0:
            min_remove += count[i] // 2
    
    return min_remove

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(remove_elements(arr))

