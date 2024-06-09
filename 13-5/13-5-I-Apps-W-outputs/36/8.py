
def f1(n, a):
    # calculate the bitwise OR of all mountains between l and r (inclusive)
    def bitwise_or(l, r):
        result = 0
        for i in range(l, r+1):
            result |= a[i]
        return result
    
    # count the number of pairs l and r such that the bitwise OR is larger than the height of any mountain at this interval
    count = 0
    for l in range(1, n):
        for r in range(l+1, n+1):
            if bitwise_or(l, r) > max(a[l:r]):
                count += 1
    return count

def f2(...):
    # implement f2 here
    pass

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    result = f1(n, a)
    print(result)

