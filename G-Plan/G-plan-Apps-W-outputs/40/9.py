
def smallest_sum_of_subarrays(n, c, a):
    a.sort()
    total_sum = sum(a)
    to_exclude = n // c
    return total_sum - sum(a[:to_exclude])

if __name__ == "__main__":
    n, c = map(int, input().split())
    a = list(map(int, input().split()))
    print(smallest_sum_of_subarrays(n, c, a))
