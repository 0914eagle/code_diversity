
def calculate_binomial_coefficient(n, k):
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)
    result = 1
    for i in range(k):
        result *= (n - i)
        result //= (i + 1)
    return result

def count_different_sets_of_points(n, points):
    y_counts = {}
    for x, y in points:
        if y not in y_counts:
            y_counts[y] = 1
        else:
            y_counts[y] += 1
    
    total_sets = 1
    for count in y_counts.values():
        total_sets *= calculate_binomial_coefficient(n, count)
    
    return total_sets

if __name__ == "__main__":
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    result = count_different_sets_of_points(n, points)
    print(result)
