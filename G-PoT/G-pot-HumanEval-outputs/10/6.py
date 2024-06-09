
def fruit_distribution(s: str, n: int) -> int:
    
    # Extracting the number of apples and oranges from the string
    apples, oranges = map(int, [x.split()[0] for x in s.split() if x.isdigit()])

    # Calculating the number of mango fruits
    mangoes = n - apples - oranges

    return mangoes
