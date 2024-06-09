
def car_race_collision(n: int) -> int:
    
    # Since the cars are moving in the same speed, they will meet at a point in the middle of the road
    # The distance between the two sets of cars is equal to the distance between the two cars that meet
    # Therefore, the number of collisions is equal to the number of pairs of cars that meet
    return n * (n - 1) // 2

