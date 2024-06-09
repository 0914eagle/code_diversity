
def eat(number: int, need: int, remaining: int) -> List[int]:
    total_eaten = number + remaining if remaining >= need else number + remaining
    carrots_left = remaining - (need - number) if remaining >= need else 0
    return [total_eaten, carrots_left]
