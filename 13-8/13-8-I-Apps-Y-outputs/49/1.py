
def compute_time(n, p, s, v):
    # Use binary search to find the optimal value of c
    left = 0
    right = 100
    while left <= right:
        mid = (left + right) // 2
        time = s * (1 + 1 / mid) / v
        if time <= n * (mid * (math.log(n) ** (mid ** 0.5)) / (p * 10 ** 9)):
            right = mid - 1
        else:
            left = mid + 1
    c = left
    
    # Compute the total time to run the algorithm and distribute the keys
    time = s * (1 + 1 / c) / v + n * (c * (math.log(n) ** (c ** 0.5)) / (p * 10 ** 9))
    
    return time, c

def main():
    n, p, s, v = map(float, input().split())
    time, c = compute_time(n, p, s, v)
    print(f"{time:.6f} {c:.6f}")

if __name__ == '__main__':
    main()

