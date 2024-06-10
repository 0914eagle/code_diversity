
def string_sequence(n: int) -> str:
    result = ""
    for i in range(n + 1):
        result += str(i) + " "
    return result.strip()

n = int(input())
print(string_sequence(n))
