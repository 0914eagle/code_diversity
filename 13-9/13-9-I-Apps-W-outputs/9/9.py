
def get_maximum_distance(n, x, a, b):
    if x == 0:
        return abs(a - b)
    
    distances = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                distances.append(abs(i - j))
    
    distances.sort(reverse=True)
    
    for i in range(x):
        distance_1 = distances[a - 1]
        distance_2 = distances[b - 1]
        if distance_1 > distance_2:
            distances[b - 1] = distance_1
            distances[a - 1] = distance_2
        else:
            break
    
    return distances[b - 1]

def main():
    t = int(input())
    for i in range(t):
        n, x, a, b = map(int, input().split())
        print(get_maximum_distance(n, x, a, b))

if __name__ == '__main__':
    main()

