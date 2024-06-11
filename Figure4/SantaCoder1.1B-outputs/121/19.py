def solution(lst):
    
    return sum([x for x in lst if x % 2 == 0])


if __name__ == "__main__":
    print(solution([5, 8, 7, 1]))
    print(solution([3, 3, 3, 3, 3]))
    print(solution([30, 13, 24, 321]))
