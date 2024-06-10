
def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    while b > 0:
        a, b = b, a % b
    return a

def max_lcm(arr):
    n = len(arr)
    max_val = 0
    for i in range(n):
        for j in range(i+1, n):
            val = lcm(arr[i], arr[j])
            if val > max_val:
                max_val = val
    return max_val

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_lcm(arr))

if __name__ == '__main__':
    main()

