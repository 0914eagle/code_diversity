
def sum_to_n(n: int) -> int:
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i
    return total_sum

n = int(input())
print(sum_to_n(n))
