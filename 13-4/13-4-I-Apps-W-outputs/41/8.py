
def get_bus_route(n, t, s, d):
    # Find the first bus route that arrives at or after the given time
    for i in range(n):
        if s[i] <= t:
            return i
    
    # If no bus route arrives at or after the given time, return -1
    return -1

def main():
    n, t = map(int, input().split())
    s = []
    d = []
    for i in range(n):
        s_i, d_i = map(int, input().split())
        s.append(s_i)
        d.append(d_i)
    route = get_bus_route(n, t, s, d)
    print(route)

if __name__ == '__main__':
    main()

