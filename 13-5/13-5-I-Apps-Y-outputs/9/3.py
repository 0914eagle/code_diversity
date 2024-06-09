
def f1(n, a):
    # find the maximum difficulty
    max_diff = max(a)
    
    # count the number of problems with difficulty greater than twice the maximum difficulty
    count = 0
    for i in range(n-2, -1, -1):
        if a[i] > max_diff * 2:
            count += 1
        else:
            break
    
    return count + 1

def f2(n, a):
    # find the maximum difficulty
    max_diff = max(a)
    
    # count the number of problems with difficulty greater than twice the maximum difficulty
    count = 0
    for i in range(n-2, -1, -1):
        if a[i] > max_diff * 2:
            count += 1
        else:
            break
    
    return count + 1

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(f1(n, a))
    print(f2(n, a))

