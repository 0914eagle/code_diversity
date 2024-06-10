
def is_possible(n, k, q, s):
    if k == 0:
        return s == q
    
    if k == 1:
        return s == q
    
    if k == 2:
        return s == q
    
    if k == 3:
        return s == q
    
    if k == 4:
        return s == q
    
    if k == 5:
        return s == q
    
    if k == 6:
        return s == q
    
    if k == 7:
        return s == q
    
    if k == 8:
        return s == q
    
    if k == 9:
        return s == q
    
    if k == 10:
        return s == q
    
    return False

def main():
    n, k = map(int, input().split())
    q = list(map(int, input().split()))
    s = list(map(int, input().split()))
    result = is_possible(n, k, q, s)
    if result:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

