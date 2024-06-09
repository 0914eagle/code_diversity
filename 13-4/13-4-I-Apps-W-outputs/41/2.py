
def get_bus_route(n, t, s, d):
    # Find the first bus route that arrives before or at time t
    for i in range(n):
        if s[i] <= t:
            return i
    
    # If no bus route arrives before or at time t, return the first bus route
    return 0

def main():
    n, t = map(int, input().split())
    s = []
    d = []
    for i in range(n):
        s_i, d_i = map(int, input().split())
        s.append(s_i)
        d.append(d_i)
    print(get_bus_route(n, t, s, d))

if __name__ == '__main__':
    main()

