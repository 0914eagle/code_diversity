
def triangle_area(a: int, h: int) -> float:
    return 0.5 * a * h

if __name__ == "__main__":
    side_length, height = map(int, input().split())
    result = triangle_area(side_length, height)
    print(result)
