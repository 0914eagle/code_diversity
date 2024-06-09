
def get_input():
    n = int(input())
    return n

def solve(n):
    a = list(range(1, n+1))
    a += a
    import random
    random.shuffle(a)
    return a

def get_output(a):
    return ' '.join(map(str, a))

if __name__ == '__main__':
    n = get_input()
    a = solve(n)
    print(get_output(a))

