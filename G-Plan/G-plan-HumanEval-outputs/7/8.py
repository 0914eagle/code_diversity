
def get_max_triples(n: int) -> int:
    def calculate_remainder(num):
        return num % 3

    a = [i * i - i + 1 for i in range(1, n + 1)]
    remainder_count = {0: 0, 1: 0, 2: 0}
    total_count = 0

    for num in a:
        remainder = calculate_remainder(num)
        remainder_count[remainder] += 1

    total_count += remainder_count[0] * (remainder_count[0] - 1) * (remainder_count[0] - 2) // 6  # Counting triples with all remainders 0
    total_count += remainder_count[1] * remainder_count[2] * remainder_count[0]  # Counting triples with remainders 1, 2, 0
    total_count += remainder_count[0] * (remainder_count[0] - 1) // 2 * remainder_count[1]  # Counting triples with remainders 0, 0, 1
    total_count += remainder_count[0] * (remainder_count[0] - 1) // 2 * remainder_count[2]  # Counting triples with remainders 0, 0, 2

    return total_count

n = int(input())
print(get_max_triples(n))
