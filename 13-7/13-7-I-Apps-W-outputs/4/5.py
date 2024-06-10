
def get_allowed_values(k, d):
    allowed_values = []
    for i in range(k):
        allowed_values.append(i * (d // k))
    return allowed_values

def get_sum_of_squared_errors(allowed_values, pixel_values):
    sum_of_squared_errors = 0
    for pixel_value in pixel_values:
        min_distance = float('inf')
        for allowed_value in allowed_values:
            distance = (pixel_value - allowed_value) ** 2
            if distance < min_distance:
                min_distance = distance
        sum_of_squared_errors += min_distance
    return sum_of_squared_errors

def main():
    d, k = map(int, input().split())
    pixel_values = []
    for _ in range(d):
        r, p = map(int, input().split())
        pixel_values += [r] * p
    allowed_values = get_allowed_values(k, d)
    print(get_sum_of_squared_errors(allowed_values, pixel_values))

if __name__ == '__main__':
    main()

