def solution(lst):
    
    return sum(lst[i] for i in range(len(lst)) if i % 2 == 1)


if __name__ == "__main__":
    print(solution([5, 8, 7