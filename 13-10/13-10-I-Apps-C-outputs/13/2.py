
def get_average_visitors(n, a, p):
    
    total_visitors = 0
    for i in range(1, n+1):
        total_visitors += get_visitors(i, a, p)
    return total_visitors / n

def get_visitors(n, a, p):
    
    if n == 0:
        return 0
    total_size = sum(a[:n])
    if total_size > p:
        return 0
    return 1 + get_visitors(n-1, a, p)

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    p = int(input())
    print(get_average_visitors(n, a, p))

