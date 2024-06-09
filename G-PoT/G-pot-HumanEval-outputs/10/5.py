
def fruit_distribution(s: str, n: int) -> int:
    
    # Extracting the number of apples and oranges from the input string
    parts = s.split()
    apples = int(parts[0]) if 'apples' in s else 0
    oranges = int(parts[-2]) if 'oranges' in s else 0

    # Calculating the number of mango fruits
    mangoes = n - apples - oranges
    return mangoes
