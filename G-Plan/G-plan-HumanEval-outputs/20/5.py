
def string_sequence(n: int) -> str:
    def generate_sequence(n: int) -> str:
        sequence = ""
        for i in range(n + 1):
            sequence += str(i) + " "
        return sequence.strip()

    return generate_sequence(n)

if __name__ == "__main__":
    n = int(input())
    print(string_sequence(n))
