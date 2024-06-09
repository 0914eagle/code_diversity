
def f1(n, a, b):
    # find the k value that maximizes the number of finalists
    k = 0
    while k < n:
        finalists = set(a[:k] + b[:k])
        if len(finalists) == n:
            break
        k += 1
    
    # determine the finalists
    finalists = set(a[:k] + b[:k])
    
    # determine the non-finalists
    non_finalists = set(a[k:] + b[k:])
    
    # create the output strings
    output1 = "".join("1" if i in finalists else "0" for i in a)
    output2 = "".join("1" if i in finalists else "0" for i in b)
    
    return output1, output2

def f2(n, a, b):
    # find the k value that minimizes the number of non-finalists
    k = n
    while k > 0:
        finalists = set(a[:k] + b[:k])
        non_finalists = set(a[k:] + b[k:])
        if len(non_finalists) == 0:
            break
        k -= 1
    
    # determine the finalists
    finalists = set(a[:k] + b[:k])
    
    # determine the non-finalists
    non_finalists = set(a[k:] + b[k:])
    
    # create the output strings
    output1 = "".join("1" if i in finalists else "0" for i in a)
    output2 = "".join("1" if i in finalists else "0" for i in b)
    
    return output1, output2

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    output1, output2 = f1(n, a, b)
    print(output1)
    print(output2)

