def solution(lst):
    
    return sum(x for x in lst if x % 2 == 1)


if __name__ == "__main__":
    print(solution([5, 8, 7, 1]))
    print(