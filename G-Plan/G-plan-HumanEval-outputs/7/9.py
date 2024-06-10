
def get_max_triples(n: int) -> int:
    def calculate_remainder(num):
        return num % 3

    def count_valid_triples(remainder_count):
        total_count = 0
        for i in range(3):
            total_count += remainder_count[i] * (remainder_count[i] - 1) * (remainder_count[i] - 2) // 6
        return total_count

    a = [i * i - i + 1 for i in range(1, n + 1)]
    remainder_count = [0, 0, 0]
    for num in a:
        remainder_count[calculate_remainder(num)] += 1

    return count_valid_triples(remainder_count)

n = int(input())
print(get_max_triples(n))
