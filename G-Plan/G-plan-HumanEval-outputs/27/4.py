
def count_collisions(n: int) -> int:
    return n * (n - 1) // 2

def car_race_collision(n: int) -> int:
    return count_collisions(n)

if __name__ == "__main__":
    n = int(input())
    print(car_race_collision(n))
