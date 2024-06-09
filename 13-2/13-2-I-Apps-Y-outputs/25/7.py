
def solve():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    while all(a % 2 == 0 for a in A):
        count += 1
        A = [a // 2 for a in A]
    return count

