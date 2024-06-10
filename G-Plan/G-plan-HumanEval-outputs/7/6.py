
def get_max_triples(n: int) -> int:
    def calculate_element(i: int) -> int:
        return i * i - i + 1

    def count_valid_triples(remainder_count: dict) -> int:
        total_count = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if (a[i] + a[j] + a[k]) % 3 == 0:
                        total_count += 1
        return total_count

    a = [calculate_element(i) for i in range(1, n)]
    remainder_count = {0: 0, 1: 0, 2: 0}
    for element in a:
        remainder_count[element % 3] += 1

    total_count = count_valid_triples(remainder_count)
    return total_count

n = int(input())
print(get_max_triples(n))
