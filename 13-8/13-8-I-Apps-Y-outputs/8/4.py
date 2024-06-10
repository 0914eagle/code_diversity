
def get_fatigue(x, umbrellas, rain_segments):
    fatigue = 0
    for i in range(len(rain_segments)):
        if x >= rain_segments[i][0] and x <= rain_segments[i][1]:
            fatigue += sum(umbrellas)
            break
    return fatigue

def pick_up_umbrella(x, umbrellas, rain_segments):
    for i in range(len(rain_segments)):
        if x >= rain_segments[i][0] and x <= rain_segments[i][1]:
            umbrellas.append(i)
            break
    return umbrellas

def throw_away_umbrella(x, umbrellas, rain_segments):
    for i in range(len(rain_segments)):
        if x >= rain_segments[i][0] and x <= rain_segments[i][1]:
            umbrellas.remove(i)
            break
    return umbrellas

def solve(a, n, m, rain_segments, umbrellas):
    total_fatigue = 0
    for x in range(a):
        fatigue = get_fatigue(x, umbrellas, rain_segments)
        if fatigue > 0:
            total_fatigue += fatigue
            umbrellas = throw_away_umbrella(x, umbrellas, rain_segments)
        else:
            umbrellas = pick_up_umbrella(x, umbrellas, rain_segments)
    return total_fatigue

if __name__ == '__main__':
    a, n, m = map(int, input().split())
    rain_segments = []
    for i in range(n):
        l, r = map(int, input().split())
        rain_segments.append([l, r])
    umbrellas = []
    for i in range(m):
        x, p = map(int, input().split())
        umbrellas.append(p)
    print(solve(a, n, m, rain_segments, umbrellas))

