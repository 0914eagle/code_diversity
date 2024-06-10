
def get_distance(distances, s, t):
    n = len(distances)
    if s == t:
        return 0
    if s > t:
        s, t = t, s
    total_distance = 0
    for i in range(s, t):
        total_distance += distances[i]
    for i in range(t, n):
        total_distance += distances[i]
    return total_distance

def main():
    n = int(input())
    distances = [int(x) for x in input().split()]
    s, t = map(int, input().split())
    print(get_distance(distances, s, t))

if __name__ == '__main__':
    main()

