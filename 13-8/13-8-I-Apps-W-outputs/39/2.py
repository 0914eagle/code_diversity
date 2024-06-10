
def get_lcm(a, b):
    
    if a == 0 or b == 0:
        return 0
    else:
        return a * b // gcd(a, b)

def gcd(a, b):
    
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def get_max_lcm(arr):
    
    n = len(arr)
    max_lcm = 0
    for i in range(n):
        for j in range(i+1, n):
            lcm = get_lcm(arr[i], arr[j])
            if lcm > max_lcm:
                max_lcm = lcm
    return max_lcm

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(get_max_lcm(arr))

