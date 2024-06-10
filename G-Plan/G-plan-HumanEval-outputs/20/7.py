
def string_sequence(n: int) -> str:
    sequence = ' '.join(str(i) for i in range(n + 1))
    return sequence

if __name__ == "__main__":
    n = int(input())
    result = string_sequence(n)
    print(result)
