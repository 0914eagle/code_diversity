
def extract_fruit_counts(s):
    counts = s.split()
    apples = int(counts[0]) if counts[0].isdigit() else 0
    oranges = int(counts[-2]) if counts[-2].isdigit() else 0
    return apples, oranges

def fruit_distribution(s: str, n: int) -> int:
    apples, oranges = extract_fruit_counts(s)
    mangoes = n - apples - oranges
    return mangoes

if __name__ == "__main__":
    s, n = input().split(', ')
    n = int(n)
    result = fruit_distribution(s, n)
    print(result)
