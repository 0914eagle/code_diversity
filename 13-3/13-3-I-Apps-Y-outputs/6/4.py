
def get_magnitude(estimate):
    return len(str(estimate))

if __name__ == '__main__':
    num_cases = int(input())
    for _ in range(num_cases):
        estimate = int(input())
        print(get_magnitude(estimate))

