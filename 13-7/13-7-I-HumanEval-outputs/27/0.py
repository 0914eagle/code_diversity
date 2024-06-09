
def fruit_distribution(s: str, n: int) -> int:
    
    # your code here
    apples = 0
    oranges = 0
    mangoes = 0
    for i in s.split(" "):
        if i.isdigit():
            if "apple" in s:
                apples = int(i)
            elif "orange" in s:
                oranges = int(i)
            else:
                mangoes = int(i)
    return n - apples - oranges - mangoes

