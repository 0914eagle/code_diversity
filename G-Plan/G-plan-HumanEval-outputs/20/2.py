
def string_sequence(n: int) -> str:
    sequence = [str(num) for num in range(n + 1)]
    return ' '.join(sequence)

if __name__ == "__main__":
    n = int(input())
    print(string_sequence(n))
