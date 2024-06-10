
def get_digits_count(estimate):
    return len(str(estimate))

def get_magnitude(estimate):
    return get_digits_count(estimate)

if __name__ == '__main__':
    num_cases = int(input())
    for _ in range(num_cases):
        estimate = int(input())
        print(get_magnitude(estimate))

