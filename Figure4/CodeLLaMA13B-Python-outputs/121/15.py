def solution(lst):
    
    if len(lst) == 0:
        return 0
    else:
        return lst[::2][1::2].sum()


if __name__ == "__main__":
    print(solution([5, 8, 7, 1]))
    print(solution([3, 3, 3, 3, 3]))
    print(solution([30, 13, 24, 321]))
