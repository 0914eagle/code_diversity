
def get_min_fatigue(a, n, m, rain_segments, umbrellas):
    # Initialize a list to store the minimum fatigue at each point
    min_fatigue = [0] * (a + 1)
    # Loop through each point from 0 to a
    for x in range(a + 1):
        # If the point is not in the rain, the minimum fatigue is 0
        if x not in rain_segments:
            min_fatigue[x] = 0
        # Otherwise, find the minimum fatigue by trying all possible umbrellas
        else:
            min_fatigue[x] = float('inf')
            for umbrella in umbrellas:
                # If the umbrella is not at the current point, skip it
                if umbrella[0] != x:
                    continue
                # Calculate the fatigue by adding the weight of the umbrella to the minimum fatigue at the previous point
                fatigue = umbrella[1] + min_fatigue[x - 1]
                # Update the minimum fatigue if the current fatigue is less than the previous minimum fatigue
                if fatigue < min_fatigue[x]:
                    min_fatigue[x] = fatigue
    # Return the minimum fatigue at the end point
    return min_fatigue[a]

def solve(a, n, m, rain_segments, umbrellas):
    # If the end point is in the rain, it is not possible to reach it
    if a in rain_segments:
        return -1
    # Otherwise, find the minimum fatigue by trying all possible umbrellas
    min_fatigue = float('inf')
    for umbrella in umbrellas:
        # If the umbrella is not at the end point, skip it
        if umbrella[0] != a:
            continue
        # Calculate the fatigue by adding the weight of the umbrella to the minimum fatigue at the previous point
        fatigue = umbrella[1] + get_min_fatigue(a - 1, n, m, rain_segments, umbrellas)
        # Update the minimum fatigue if the current fatigue is less than the previous minimum fatigue
        if fatigue < min_fatigue:
            min_fatigue = fatigue
    # Return the minimum fatigue
    return min_fatigue

def main():
    a, n, m = map(int, input().split())
    rain_segments = set()
    for _ in range(n):
        l, r = map(int, input().split())
        rain_segments.add((l, r))
    umbrellas = []
    for _ in range(m):
        x, p = map(int, input().split())
        umbrellas.append((x, p))
    print(solve(a, n, m, rain_segments, umbrellas))

if __name__ == '__main__':
    main()

