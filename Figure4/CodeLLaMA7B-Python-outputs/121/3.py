def solution(lst):
    
    odd_sum = 0
    for i in range(len(lst)):
        if i % 2 == 0:
            if lst[i] % 2 != 0:
                odd_sum += lst[i]
    return odd_sum


print(solution([5, 8, 7, 1]))
print(solution([3, 3, 3, 3, 3]))
print(solution([30, 13, 24, 321]))
