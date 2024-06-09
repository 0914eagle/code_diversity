
def f1(n, a):
    # find the maximum difficulty
    max_diff = max(a)
    
    # count the number of problems with difficulty greater than the maximum difficulty
    count = 0
    for i in range(n):
        if a[i] > max_diff:
            count += 1
    
    return count

def f2(n, a):
    # find the maximum difficulty
    max_diff = max(a)
    
    # count the number of problems with difficulty greater than the maximum difficulty
    count = 0
    for i in range(n):
        if a[i] > max_diff:
            count += 1
    
    return count

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(f1(n, a))
    print(f2(n, a))

