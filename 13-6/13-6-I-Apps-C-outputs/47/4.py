
def is_beautiful(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] == arr[j] or arr[i]+1 == arr[j] or arr[j] == arr[i]+1:
                return True
    return False

def get_max_amount(coupons):
    max_amount = 0
    for coupon in coupons:
        q, w = coupon
        if q == 1:
            max_amount += w
        else:
            max_amount += w*(q-1)
    return max_amount

def solve(n, m, coupons):
    max_amount = 0
    for i in range(1, n+1):
        arr = list(range(1, i+1))
        if is_beautiful(arr):
            max_amount = max(max_amount, get_max_amount(coupons))
    return max_amount

if __name__ == '__main__':
    n, m = map(int, input().split())
    coupons = []
    for _ in range(m):
        q, w = map(int, input().split())
        coupons.append((q, w))
    print(solve(n, m, coupons))

