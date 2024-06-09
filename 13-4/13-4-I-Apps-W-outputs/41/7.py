
def get_bus_route(n, t, s, d):
    # Find the first bus route that arrives after time t
    for i in range(n):
        if s[i] > t:
            return i
    
    # If no bus route arrives after time t, return the first bus route
    return 0

def main():
    n, t = map(int, input().split())
    s = []
    d = []
    for i in range(n):
        si, di = map(int, input().split())
        s.append(si)
        d.append(di)
    print(get_bus_route(n, t, s, d))

if __name__ == '__main__':
    main()

