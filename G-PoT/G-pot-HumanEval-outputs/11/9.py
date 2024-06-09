
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

    collatz_numbers = collatz_sequence(n)
    odd_numbers = [num for num in collatz_numbers if num % 2 != 0]
    return sorted(odd_numbers)
