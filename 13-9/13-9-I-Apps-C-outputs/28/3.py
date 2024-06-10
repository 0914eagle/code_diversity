
def get_division(towns, universities, roads):
    # Implement your solution here
    return division

def get_total_distance(division):
    # Implement your solution here
    return total_distance

if __name__ == '__main__':
    n, k = map(int, input().split())
    towns = set(map(int, input().split()))
    universities = set(map(int, input().split()))
    roads = []
    for _ in range(n - 1):
        x, y = map(int, input().split())
        roads.append((x, y))
    
    division = get_division(towns, universities, roads)
    total_distance = get_total_distance(division)
    print(total_distance)

