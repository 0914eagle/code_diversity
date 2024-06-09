
def solve(A, B, K):
    takahashi_cookies, aoki_cookies = A, B
    for i in range(K):
        if takahashi_cookies > 0:
            takahashi_cookies -= 1
        elif aoki_cookies > 0:
            aoki_cookies -= 1
    return takahashi_cookies, aoki_cookies

