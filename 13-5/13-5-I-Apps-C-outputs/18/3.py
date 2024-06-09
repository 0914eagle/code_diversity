
def read_input():
    n, m = map(int, input().split())
    beacons = []
    for _ in range(n):
        x, y = map(int, input().split())
        beacons.append((x, y))
    mountains = []
    for _ in range(m):
        x, y, r = map(int, input().split())
        mountains.append((x, y, r))
    return n, m, beacons, mountains

def within_sight(beacon, beacons, mountains):
    for other in beacons:
        if other != beacon and not blocked(beacon, other, mountains):
            yield other

def blocked(beacon1, beacon2, mountains):
    for mountain in mountains:
        if circle_line_intersection(mountain, beacon1, beacon2):
            return True
    return False

def circle_line_intersection(circle, p1, p2):
    dx, dy = p2[0] - p1[0], p2[1] - p1[1]
    d = (dx**2 + dy**2)**0.5
    a = (dx*dy)**2 - (d**2 - circle[2]**2)*(dx**2 + dy**2)
    b = 2*(dx*(p1[1]-circle[1]) + dy*(p1[0]-circle[0]))
    c = (p1[0]-circle[0])**2 + (p1[1]-circle[1])**2 - circle[2]**2
    det = b**2 - 4*a*c
    if det < 0:
        return False
    else:
        return True

def f1(n, m, beacons, mountains):
    visited = set()
    queue = [beacons[0]]
    while queue:
        beacon = queue.pop(0)
        if beacon not in visited:
            visited.add(beacon)
            queue.extend(within_sight(beacon, beacons, mountains))
    return len(visited) == n

def f2(n, m, beacons, mountains):
    visited = set()
    queue = [beacons[0]]
    while queue:
        beacon = queue.pop(0)
        if beacon not in visited:
            visited.add(beacon)
            queue.extend(within_sight(beacon, beacons, mountains))
    return len(visited) == n

if __name__ == '__main__':
    n, m, beacons, mountains = read_input()
    print(f2(n, m, beacons, mountains))

