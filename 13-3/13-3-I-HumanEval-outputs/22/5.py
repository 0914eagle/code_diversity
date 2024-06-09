
def car_race_collision(n: int) -> int:
    
    # Since the cars are moving in the same speed, they will collide after a distance of n.
    # Therefore, the number of collisions is equal to the number of pairs of cars that collide.
    # There are n pairs of cars in total, so the number of collisions is n * (n - 1) / 2.
    return n * (n - 1) // 2

