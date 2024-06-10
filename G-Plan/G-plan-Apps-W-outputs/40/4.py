
def calculate_sum(a, c):
    n = len(a)
    a.sort()
    sum_values = 0
    for i in range(n - n // c):
        sum_values += a[i]
    return sum_values

def find_smallest_sum_of_subarrays(n, c, a):
    return calculate_sum(a, c)

if __name__ == "__main__":
    n, c = map(int, input().split())
    a = list(map(int, input().split()))
    result = find_smallest_sum_of_subarrays(n, c, a)
    print(result)
