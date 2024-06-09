
def get_input():
    N = int(input())
    lamps = []
    for i in range(N):
        x, y, e = map(int, input().split())
        lamps.append((x, y, e))
    return N, lamps

def find_balancing_line(N, lamps):
    # Initialize the balancing line as a set of two points
    balancing_line = set()
    
    # Loop through each lamp and check if it is on the balancing line
    for lamp in lamps:
        x, y, e = lamp
        
        # If the lamp is on the balancing line, add it to the set
        if x == y or x == N-y or x+y == N:
            balancing_line.add(lamp)
    
    # If the set of lamps on the balancing line is not empty, return the length of the balancing line
    if balancing_line:
        return len(balancing_line)
    
    # If the set of lamps on the balancing line is empty, return "IMPOSSIBLE"
    return "IMPOSSIBLE"

def main():
    N, lamps = get_input()
    print(find_balancing_line(N, lamps))

if __name__ == '__main__':
    main()

