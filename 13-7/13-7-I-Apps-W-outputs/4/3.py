
def get_allowed_values(k):
    return list(range(k))

def get_squared_errors(allowed_values, pixel_values):
    squared_errors = 0
    for pixel_value in pixel_values:
        closest_value = min(allowed_values, key=lambda x: abs(x - pixel_value))
        squared_errors += (pixel_value - closest_value) ** 2
    return squared_errors

def get_min_squared_errors(k, pixel_values):
    allowed_values = get_allowed_values(k)
    return min(get_squared_errors(allowed_values, pixel_values) for allowed_values in itertools.permutations(allowed_values))

def main():
    d, k = map(int, input().split())
    pixel_values = []
    for _ in range(d):
        r, p = map(int, input().split())
        pixel_values.extend([r] * p)
    print(get_min_squared_errors(k, pixel_values))

if __name__ == '__main__':
    main()

