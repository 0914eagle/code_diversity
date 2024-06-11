def solution(lst):
    
    odd_sum = 0
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 != 0:
            odd_sum += lst[i]
    return odd_sum


