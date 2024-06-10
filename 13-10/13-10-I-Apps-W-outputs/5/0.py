
def get_input():
    n = int(input())
    distances = [int(x) for x in input().split()]
    s, t = map(int, input().split())
    return n, distances, s, t

def get_shortest_distance(distances, s, t):
    if s == t:
        return 0
    
    shortest_distance = float('inf')
    for i in range(len(distances)):
        distance = distances[i]
        if s + i - 1 == t or t + i - 1 == s:
            shortest_distance = min(shortest_distance, distance)
    
    return shortest_distance

def main():
    n, distances, s, t = get_input()
    print(get_shortest_distance(distances, s, t))

if __name__ == '__main__':
    main()

