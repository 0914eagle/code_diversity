
def f1(a, b, s):
    if a <= b:
        return "NO"
    
    if s.count(".") < b:
        return "NO"
    
    if s.count(".") == b:
        return "YES"
    
    if s.count(".") > b:
        return "YES"

def f2(q):
    for _ in range(q):
        a, b = map(int, input().split())
        s = input()
        print(f1(a, b, s))

if __name__ == '__main__':
    q = int(input())
    f2(q)

