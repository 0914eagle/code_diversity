
def fruit_distribution(s: str, n: int) -> int:
    
    # Extract the number of apples and oranges from the input string
    apples, oranges = 0, 0
    for word in s.split():
        if word.isdigit():
            if 'apple' in s:
                apples = int(word)
            elif 'orange' in s:
                oranges = int(word)
    
    # Calculate the number of mango fruits
    mangoes = n - apples - oranges
    return mangoes
