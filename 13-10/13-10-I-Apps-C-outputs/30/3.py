
def get_max_minions(n, m, r):
    # find the minimum radius that can destroy all minions without touching any village
    min_radius = get_min_radius(n, m, r)
    # find the maximum radius that can destroy all minions without touching any village
    max_radius = get_max_radius(n, m, r)
    # return the maximum number of minions that can be destroyed with the minimum radius
    return get_num_minions(n, m, min_radius)

def get_min_radius(n, m, r):
    # find the distance between the first minion and the first village
    dist = get_distance(0, 0, m, 0)
    # find the minimum radius that can destroy all minions without touching any village
    min_radius = dist + 1
    for i in range(n):
        for j in range(m):
            # find the distance between the current minion and the current village
            dist = get_distance(m, j, n, i)
            # update the minimum radius if the current distance is smaller than the current minimum radius
            if dist < min_radius:
                min_radius = dist
    return min_radius

def get_max_radius(n, m, r):
    # find the distance between the first minion and the first village
    dist = get_distance(0, 0, m, 0)
    # find the maximum radius that can destroy all minions without touching any village
    max_radius = dist + 1
    for i in range(n):
        for j in range(m):
            # find the distance between the current minion and the current village
            dist = get_distance(m, j, n, i)
            # update the maximum radius if the current distance is larger than the current maximum radius
            if dist > max_radius:
                max_radius = dist
    return max_radius

def get_num_minions(n, m, r):
    # find the number of minions that can be destroyed within the given radius
    num_minions = 0
    for i in range(n):
        for j in range(m):
            # find the distance between the current minion and the center of the area of effect
            dist = get_distance(m, j, 0, 0)
            # count the current minion if it is within the given radius
            if dist <= r:
                num_minions += 1
    return num_minions

def get_distance(x1, y1, x2, y2):
    # find the Euclidean distance between two points
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    r = int(input())
    print(get_max_minions(n, m, r))

