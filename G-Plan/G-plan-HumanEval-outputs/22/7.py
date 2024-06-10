
def extract_fruit_counts(s):
    counts = s.split()
    apples = int(counts[0])
    oranges = int(counts[3])
    return apples, oranges

def fruit_distribution(s: str, n: int) -> int:
    apples, oranges = extract_fruit_counts(s)
    mangoes = n - apples - oranges
    return mangoes

if __name__ == "__main__":
    s, n = input().split(', ')
    result = fruit_distribution(s, int(n))
    print(result)
