
def get_max_triples(n: int) -> int:
    def calculate_element(i: int) -> int:
        return i * i - i + 1

    def count_valid_triples(arr: list) -> int:
        count = 0
        remainder_count = {0: 0, 1: 0, 2: 0}
        
        for num in arr:
            remainder = num % 3
            remainder_count[remainder] += 1

        count += remainder_count[0] * (remainder_count[0] - 1) * (remainder_count[0] - 2) // 6
        count += remainder_count[1] * remainder_count[2] * remainder_count[0]
        count += remainder_count[1] * (remainder_count[1] - 1) * (remainder_count[1] - 2) // 6
        count += remainder_count[2] * (remainder_count[2] - 1) * (remainder_count[2] - 2) // 6

        return count

    a = [calculate_element(i) for i in range(1, n + 1)]
    return count_valid_triples(a)

n = int(input())
print(get_max_triples(n))
