
def eat(number: int, need: int, remaining: int) -> List[int]:
    total_eaten = number + need
    if remaining >= need:
        remaining_carrots = remaining - need
    else:
        remaining_carrots = 0
    return [total_eaten, remaining_carrots]
