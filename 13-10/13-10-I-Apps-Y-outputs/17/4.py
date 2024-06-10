
def get_lexicographical_order(p):
    
    n = len(p)
    order = 1
    for i in range(n-1):
        for j in range(i+1, n):
            if p[i] > p[j]:
                order += 1
    return order

def get_absolute_difference(p, q):
    
    return abs(get_lexicographical_order(p) - get_lexicographical_order(q))

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    print(get_absolute_difference(p, q))

if __name__ == '__main__':
    main()

