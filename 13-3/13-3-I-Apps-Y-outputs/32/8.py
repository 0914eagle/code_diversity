
def solve(numbers):
    modulo_42 = set()
    for num in numbers:
        modulo_42.add(num % 42)
    return len(modulo_42)

