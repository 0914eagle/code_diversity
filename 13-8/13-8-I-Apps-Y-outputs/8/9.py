
def get_umbrella_strategy(a, n, m, segments, umbrellas):
    # Initialize the optimal strategy as a list of tuples (umbrella index, segment index)
    strategy = []
    
    # Loop through each segment and find the first umbrella that covers it
    for i in range(n):
        segment = segments[i]
        for j in range(m):
            umbrella = umbrellas[j]
            if umbrella[0] <= segment[0] and segment[1] <= umbrella[1]:
                strategy.append((j, i))
                break
    
    # Return the optimal strategy
    return strategy

def get_total_fatigue(a, n, m, segments, umbrellas, strategy):
    # Initialize the total fatigue as 0
    total_fatigue = 0
    
    # Loop through each segment and calculate the fatigue for each umbrella
    for i in range(n):
        segment = segments[i]
        umbrella_index, _ = strategy[i]
        umbrella = umbrellas[umbrella_index]
        fatigue = umbrella[1] * (segment[1] - segment[0])
        total_fatigue += fatigue
    
    # Return the total fatigue
    return total_fatigue

def main():
    a, n, m = map(int, input().split())
    segments = []
    umbrellas = []
    for i in range(n):
        l, r = map(int, input().split())
        segments.append((l, r))
    for i in range(m):
        x, p = map(int, input().split())
        umbrellas.append((x, p))
    strategy = get_umbrella_strategy(a, n, m, segments, umbrellas)
    total_fatigue = get_total_fatigue(a, n, m, segments, umbrellas, strategy)
    print(total_fatigue)

if __name__ == '__main__':
    main()

