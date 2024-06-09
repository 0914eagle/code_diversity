
def fruit_distribution(s: str, n: int) -> int:
    
    # Extracting the number of apples and oranges from the input string
    apples = int(s.split(' ')[0])
    oranges = int(s.split(' ')[3])

    # Calculating the number of mango fruits
    mango = n - apples - oranges
    return mango
