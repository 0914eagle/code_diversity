
def f1(N, M, places, roads):
    # your code here
    return trips

def f2(N, M, places, roads):
    # your code here
    return trips

if __name__ == '__main__':
    N, M = map(int, input().split())
    places = set(map(int, input().split()))
    roads = []
    for _ in range(M):
        f, t = map(int, input().split())
        roads.append((f, t))
    trips = f1(N, M, places, roads)
    print(trips)

