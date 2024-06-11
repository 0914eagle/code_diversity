def solution(lst):
    
    odd_sum = 0
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 != 0:
            odd_sum += lst[i]
    return odd_sum


# solution([5, 8, 7, 1])
# solution([3, 3, 3, 3, 3])
# solution([30, 13, 24, 321])
