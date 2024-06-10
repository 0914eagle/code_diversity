
def is_possible(arr):
    n = len(arr)
    if n == 1:
        return True
    if n == 2:
        return arr[0] == arr[1]
    for i in range(n-1):
        for j in range(i+1, n):
            if abs(arr[i] - arr[j]) <= 1:
                return True
    return False

def solve(arr):
    if is_possible(arr):
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    num_cases = int(input())
    for _ in range(num_cases):
        n = int(input())
        arr = list(map(int, input().split()))
        print(solve(arr))

