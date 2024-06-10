
def f(n):
    return int(str(n)[0]) * int(str(n)[1:])

def find_smallest_solution(b, n):
    for i in range(1, 1000000000):
        if f(i) == n:
            return i
    return "impossible"

if __name__ == '__main__':
    b, n = map(int, input().split())
    print(find_smallest_solution(b, n))

