
def is_beautiful(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] == arr[j] or arr[i]+1 == arr[j] or arr[j] == arr[i]+1:
                return True
    return False

def get_maximum_amount(n, m, coupons):
    max_amount = 0
    for i in range(m):
        q, w = coupons[i]
        if q <= n:
            max_amount += w
    return max_amount

def main():
    n, m = map(int, input().split())
    coupons = []
    for i in range(m):
        q, w = map(int, input().split())
        coupons.append((q, w))
    max_amount = get_maximum_amount(n, m, coupons)
    print(max_amount)

if __name__ == '__main__':
    main()

