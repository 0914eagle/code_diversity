
def f1(q):
    # Your code here
    return "YES"

def f2(q):
    # Your code here
    return "NO"

if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        a, b = map(int, input().split())
        s = input()
        print(f1(a, b, s))

