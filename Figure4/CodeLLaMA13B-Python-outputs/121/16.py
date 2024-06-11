def solution(lst):
    
    return sum([lst[i] for i in range(len(lst)) if i%2==0 and lst[i]%2!=0])


if __name__ == "__main__":
    print(solution([5, 8, 7, 1]))
    print(solution([3, 3, 3, 3, 3]))
    print(solution([30, 13, 24, 321]))
