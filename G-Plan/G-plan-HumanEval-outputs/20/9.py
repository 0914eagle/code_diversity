
def string_sequence(n: int) -> str:
    result = ""
    for i in range(n + 1):
        result += str(i) + " "
    return result.rstrip()

if __name__ == "__main__":
    n = int(input())
    print(string_sequence(n))
