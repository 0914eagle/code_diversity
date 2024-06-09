
def eat(number: int, need: int, remaining: int) -> List[int]:
    total_eaten = number + min(need, remaining)
    carrots_left = max(0, remaining - need)
    return [total_eaten, carrots_left]
