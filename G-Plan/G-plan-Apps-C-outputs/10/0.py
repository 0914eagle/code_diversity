
def calculate_sunlight_hours(N, buildings):
    result = []
    for x, h in buildings:
        hours = 2 * (h ** 0.5)
        result.append(f"{hours:.4f}")
    return result

if __name__ == "__main__":
    N = int(input())
    buildings = [list(map(int, input().split())) for _ in range(N)]
    output = calculate_sunlight_hours(N, buildings)
    for line in output:
        print(line)
