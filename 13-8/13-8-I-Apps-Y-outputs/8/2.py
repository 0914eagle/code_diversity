
def get_min_fatigue(a, n, m, rain_segments, umbrellas):
    # Initialize a dictionary to store the minimum fatigue at each point
    min_fatigue = {0: 0}
    for i in range(1, a + 1):
        min_fatigue[i] = float('inf')

    # Loop through each umbrella and calculate the minimum fatigue at each point
    for umbrella in umbrellas:
        x, p = umbrella
        for i in range(x, a + 1):
            min_fatigue[i] = min(min_fatigue[i], min_fatigue[i - 1] + p)

    # Loop through each rain segment and calculate the minimum fatigue at each point
    for segment in rain_segments:
        l, r = segment
        for i in range(l, r + 1):
            min_fatigue[i] = min(min_fatigue[i], min_fatigue[i - 1] + 1)

    # Return the minimum fatigue at the end point
    return min_fatigue[a]

def main():
    a, n, m = map(int, input().split())
    rain_segments = []
    for i in range(n):
        l, r = map(int, input().split())
        rain_segments.append((l, r))
    umbrellas = []
    for i in range(m):
        x, p = map(int, input().split())
        umbrellas.append((x, p))
    print(get_min_fatigue(a, n, m, rain_segments, umbrellas))

if __name__ == '__main__':
    main()

