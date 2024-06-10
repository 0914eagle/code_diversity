
def triangle_area(a: int, h: int) -> float:
    area = 0.5 * a * h
    return area

if __name__ == "__main__":
    a, h = map(int, input().split())
    result = triangle_area(a, h)
    print(result)
