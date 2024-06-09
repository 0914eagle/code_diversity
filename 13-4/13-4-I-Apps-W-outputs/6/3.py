
def get_min_time(t_s, t_f, t, n, visitors):
    # Find the earliest time that Vasya can arrive to be served
    for i in range(t_s, t_f + 1):
        if i % t == 0:
            return i
    
    # If the receptionist is free at the same time with other visitors, Vasya should queue up after the last visitor
    return (t_f - 1)

def main():
    t_s, t_f, t = map(int, input().split())
    n = int(input())
    visitors = sorted([int(x) for x in input().split()])
    print(get_min_time(t_s, t_f, t, n, visitors))

if __name__ == '__main__':
    main()

