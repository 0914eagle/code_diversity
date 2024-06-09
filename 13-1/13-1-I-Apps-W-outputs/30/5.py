
def get_shortest_dominated_subarray(arr):
    if len(arr) < 2:
        return -1
    
    counts = {}
    for num in arr:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1
    
    max_count = max(counts.values())
    max_num = [num for num, count in counts.items() if count == max_count][0]
    
    start = 0
    end = 0
    count = 0
    for i in range(len(arr)):
        if arr[i] == max_num:
            count += 1
            end = i
        else:
            if count > 0:
                if count == 1:
                    start = i - count + 1
                else:
                    start = i - count
                break
    
    if count == 0:
        return -1
    
    return end - start + 1

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        arr = list(map(int, input().split()))
        print(get_shortest_dominated_subarray(arr))

