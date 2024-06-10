
def get_input():
    n = int(input())
    distances = [int(x) for x in input().split()]
    s, t = map(int, input().split())
    return n, distances, s, t

def find_shortest_distance(distances, s, t):
    if s == t:
        return 0
    total_distances = sum(distances)
    distances = distances + distances[:s-1]
    distances.append(total_distances - distances[t-1])
    return min(distances[s-1:t] + distances[t:s-1])

def main():
    n, distances, s, t = get_input()
    print(find_shortest_distance(distances, s, t))

if __name__ == '__main__':
    main()

