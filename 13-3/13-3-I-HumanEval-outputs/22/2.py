
def car_race_collision(n: int) -> int:
    
    # The number of collisions is equal to the number of pairs of cars that cross each other
    # The number of pairs of cars that cross each other is equal to the number of cars that are moving left to right multiplied by the number of cars that are moving right to left
    # Since the cars are infinitely sturdy and strong, each pair of cars will cross each other only once
    return n * (n - 1) // 2

