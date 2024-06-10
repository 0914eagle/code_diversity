
def read_input():
    R, B = map(int, input().split())
    rebels = []
    for i in range(R):
        x, y = map(int, input().split())
        rebels.append((x, y))
    bases = []
    for i in range(B):
        x, y = map(int, input().split())
        bases.append((x, y))
    return R, B, rebels, bases

def get_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def find_matching(R, B, rebels, bases):
    matching = []
    for i in range(R):
        min_dist = float('inf')
        for j in range(B):
            dist = get_distance(rebels[i], bases[j])
            if dist < min_dist:
                min_dist = dist
                matching.append((i, j))
    return matching

def is_perfect_matching(matching):
    for i in range(len(matching)):
        for j in range(i+1, len(matching)):
            if matching[i][0] == matching[j][1] or matching[i][1] == matching[j][0]:
                return False
    return True

def solve(R, B, rebels, bases):
    matching = find_matching(R, B, rebels, bases)
    return 'Yes' if is_perfect_matching(matching) else 'No'

if __name__ == '__main__':
    R, B, rebels, bases = read_input()
    print(solve(R, B, rebels, bases))

