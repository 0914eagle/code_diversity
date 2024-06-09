
def fruit_distribution(s: str, n: int) -> int:
    
    # Extract the number of apples and oranges from the input string
    apples = int(s.split(' ')[0])
    oranges = int(s.split(' ')[-2])

    # Calculate the number of mango fruits
    mangoes = n - apples - oranges

    return mangoes
