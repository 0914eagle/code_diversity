
def eat(number: int, need: int, remaining: int) -> List[int]:
    total_eaten = number + min(need, remaining)
    remaining_carrots = max(0, remaining - need)
    return [total_eaten, remaining_carrots]
