def solution(lst):
    
    odd_sum = 0
    for i in lst:
        if i % 2 == 1:
            odd_sum += i
    return odd_sum


if __name__ == "__main__":
    print(solution([5, 8, 7, 1]))
    print(solution([3, 3, 3, 3, 3]))
    print(solution([30, 13, 24, 321]))
