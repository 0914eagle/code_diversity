
def get_bus_route(t, n, s, d):
    # Find the first bus route that arrives at or after the given time t
    for i in range(n):
        if s[i] <= t:
            return i
    
    # If no bus route arrives at or after the given time t, return -1
    return -1

def main():
    t = int(input())
    n = int(input())
    s = []
    d = []
    for i in range(n):
        si, di = map(int, input().split())
        s.append(si)
        d.append(di)
    
    route = get_bus_route(t, n, s, d)
    print(route)

if __name__ == '__main__':
    main()

