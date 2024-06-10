
def calculate_sum(a, c):
    n = len(a)
    min_sum = float('inf')
    
    for i in range(n):
        sum_val = 0
        for j in range(n):
            if j % c != i % c:
                sum_val += a[j]
        min_sum = min(min_sum, sum_val)
    
    return min_sum

if __name__ == "__main__":
    n, c = map(int, input().split())
    a = list(map(int, input().split()))
    
    result = calculate_sum(a, c)
    print(result)
