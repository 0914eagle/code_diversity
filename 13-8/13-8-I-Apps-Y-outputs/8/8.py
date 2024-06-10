
def get_optimal_fatigue(a, n, m, rain_segments, umbrellas):
    # Initialize a dictionary to store the optimal fatigue for each point
    optimal_fatigue = {0: 0}
    
    # Loop through each point from 1 to a
    for x in range(1, a + 1):
        # Get the weights of the umbrellas at point x
        weights = [umbrella[1] for umbrella in umbrellas if umbrella[0] == x]
        
        # Get the minimum fatigue for each segment that intersects with point x
        min_fatigue = float('inf')
        for segment in rain_segments:
            if segment[0] <= x and x <= segment[1]:
                min_fatigue = min(min_fatigue, sum(weights))
        
        # Get the minimum fatigue for point x by considering the minimum fatigue of all segments that intersect with point x
        optimal_fatigue[x] = min_fatigue + optimal_fatigue[x - 1]
    
    # Return the minimum fatigue for point a
    return optimal_fatigue[a]

def main():
    a, n, m = map(int, input().split())
    rain_segments = []
    umbrellas = []
    for i in range(n):
        l, r = map(int, input().split())
        rain_segments.append([l, r])
    for i in range(m):
        x, p = map(int, input().split())
        umbrellas.append([x, p])
    print(get_optimal_fatigue(a, n, m, rain_segments, umbrellas))

if __name__ == '__main__':
    main()

