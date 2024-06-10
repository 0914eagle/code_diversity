
import itertools

def get_average_visitors(n, a, p):
    
    total = 0
    count = 0
    for order in itertools.permutations(a):
        visitors = 0
        current_sum = 0
        for i in order:
            if current_sum + i <= p:
                visitors += 1
                current_sum += i
            else:
                break
        total += visitors
        count += 1
    return total / count

def main():
    n = int(input())
    a = list(map(int, input().split()))
    p = int(input())
    print(get_average_visitors(n, a, p))

if __name__ == '__main__':
    main()

