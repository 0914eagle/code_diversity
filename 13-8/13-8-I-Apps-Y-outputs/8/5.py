
def is_rain(x, rain):
    for segment in rain:
        if segment[0] <= x <= segment[1]:
            return True
    return False

def pick_umbrella(x, umbrellas, rain):
    if not is_rain(x, rain):
        return []
    for umbrella in umbrellas:
        if umbrella[0] <= x <= umbrella[1]:
            return [umbrella]
    return []

def throw_umbrella(x, umbrellas, rain):
    if not is_rain(x, rain):
        return umbrellas
    for i in range(len(umbrellas)):
        if umbrellas[i][0] <= x <= umbrellas[i][1]:
            return umbrellas[:i] + umbrellas[i+1:]
    return umbrellas

def total_fatigue(umbrellas):
    return sum(umbrella[2] for umbrella in umbrellas)

def find_min_fatigue(umbrellas, rain):
    min_fatigue = total_fatigue(umbrellas)
    for i in range(len(umbrellas)):
        umbrella = umbrellas[i]
        if not is_rain(umbrella[0], rain):
            continue
        new_umbrellas = umbrellas[:i] + umbrellas[i+1:]
        new_fatigue = total_fatigue(new_umbrellas)
        if new_fatigue < min_fatigue:
            min_fatigue = new_fatigue
    return min_fatigue

def main():
    a, n, m = map(int, input().split())
    rain = []
    for i in range(n):
        l, r = map(int, input().split())
        rain.append([l, r])
    umbrellas = []
    for i in range(m):
        x, p = map(int, input().split())
        umbrellas.append([x, x+1, p])
    umbrellas.sort(key=lambda x: x[0])
    min_fatigue = find_min_fatigue(umbrellas, rain)
    print(min_fatigue)

if __name__ == '__main__':
    main()

