
def get_max_triples(n: int) -> int:
    def calculate_element(i: int) -> int:
        return i * i - i + 1

    def count_valid_triples(remainder_count: dict) -> int:
        total_count = 0
        for remainder in remainder_count.keys():
            count = remainder_count[remainder]
            total_count += count * (count - 1) * (count - 2) // 6
        return total_count

    a = [calculate_element(i) for i in range(1, n + 1)]
    remainder_count = {0: 0, 1: 0, 2: 0}
    for num in a:
        remainder_count[num % 3] += 1

    return count_valid_triples(remainder_count)

n = int(input())
print(get_max_triples(n))
