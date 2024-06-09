
def car_race_collision(n: int) -> int:
    
    # The number of collisions is equal to the number of pairs of cars that collide
    # We can represent each car as a pair of integers (x, y), where x is the position of the car on the left side of the road and y is the position of the car on the right side of the road
    # We can generate all possible pairs of cars and count the number of pairs that collide
    return sum(1 for x in range(n) for y in range(n) if x == y)

