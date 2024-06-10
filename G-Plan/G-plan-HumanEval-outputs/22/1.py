
def extract_fruit_numbers(s):
    numbers = [int(num) for num in s.split() if num.isdigit()]
    return numbers

def fruit_distribution(s: str, n: int) -> int:
    apples, oranges = extract_fruit_numbers(s)
    mangoes = n - apples - oranges
    return mangoes

if __name__ == "__main__":
    s, n = input().split(', ')
    result = fruit_distribution(s, int(n))
    print(result)
