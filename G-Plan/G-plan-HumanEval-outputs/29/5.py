
def triangle_area(a: int, h: int) -> float:
    return 0.5 * a * h

if __name__ == "__main__":
    a, h = map(int, input().split())
    print(triangle_area(a, h))
