def solution(lst):
    
    return sum(lst[i] for i in range(len(lst)) if lst[i] % 2 == 1)


if __name__ == "__