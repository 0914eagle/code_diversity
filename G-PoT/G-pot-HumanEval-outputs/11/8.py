
from typing import List

def get_odd_collatz(n: int) -> List[int]:
    def collatz_sequence(num):
        sequence = [num]
        while num != 1:
            if num % 2 == 0:
                num = num // 2
            else:
                num = 3 * num + 1
            sequence.append(num)
        return sequence

    odd_numbers = set()
    for i in range(1, n + 1):
        sequence = collatz_sequence(i)
        for num in sequence:
            if num % 2 != 0:
                odd_numbers.add(num)

    return sorted(list(odd_numbers))
