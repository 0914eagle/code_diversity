def solution(lst):
    
    if lst == []:
        return 0
    else:
        sum = 0
        for i in range(0, len(lst), 2):
            if lst[i] % 2 != 0:
                sum += lst[i]
        return sum

print(solution([5, 8, 7, 1]))
print(solution([3, 3, 3, 3, 3]))
print(solution([30, 13, 24, 321]))