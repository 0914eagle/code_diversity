
def extract_fruit_counts(s):
    parts = s.split()
    apples = int(parts[0]) if parts[0].isdigit() else 0
    oranges = int(parts[-2]) if parts[-2].isdigit() else 0
    return apples, oranges

def fruit_distribution(s: str, n: int) -> int:
    apples, oranges = extract_fruit_counts(s)
    return n - apples - oranges

if __name__ == "__main__":
    s, n = input().split(', ')
    result = fruit_distribution(s, int(n))
    print(result)
