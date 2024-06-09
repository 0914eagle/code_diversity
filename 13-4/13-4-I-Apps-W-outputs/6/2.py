
def get_min_time(t_s, t_f, t, n, visitors):
    # Find the earliest time that Vasya can arrive to be served
    for i in range(t_s, t_f + 1):
        if i % t == 0:
            return i
    
    # If the receptionist is free at the same time as Vasya, he will be served immediately
    if t_f % t == 0:
        return t_f
    
    # If Vasya arrives at the same time as the last visitor, he will queue up after him
    return visitors[-1] + t

def main():
    t_s, t_f, t = map(int, input().split())
    n = int(input())
    visitors = sorted([int(x) for x in input().split()])
    print(get_min_time(t_s, t_f, t, n, visitors))

if __name__ == '__main__':
    main()

