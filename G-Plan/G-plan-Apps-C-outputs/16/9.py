
def count_sequences(n, prev):
    if n == 1:
        return 1
    if n < prev:
        return 0
    total_count = 0
    for i in range(1, min(n, prev) + 1):
        total_count += count_sequences(n - i, i)
    return total_count

def solve_problem(n):
    return count_sequences(n, n) % (10**9 + 7)

if __name__ == '__main__':
    n = int(input())
    result = solve_problem(n)
    print(result)
