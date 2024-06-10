
def read_input():
    d, k = map(int, input().split())
    pixels = []
    for _ in range(d):
        r, p = map(int, input().split())
        pixels.append((r, p))
    return d, k, pixels

def compute_errors(pixels, k):
    errors = []
    for r, p in pixels:
        errors.append(min([(r - v)**2 for v in range(k+1)]) * p)
    return sum(errors)

def find_optimal_k(d, k, pixels):
    errors = []
    for i in range(1, k+1):
        errors.append(compute_errors(pixels, i))
    return errors.index(min(errors)) + 1

def main():
    d, k, pixels = read_input()
    optimal_k = find_optimal_k(d, k, pixels)
    print(compute_errors(pixels, optimal_k))

if __name__ == '__main__':
    main()

