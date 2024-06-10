
def can_reach_end(n, m, d, c):
    # Initialize variables
    platforms = [[0, 0]] + [[i, c[i-1]] for i in range(1, m+1)] + [[n+1, 0]]
    positions = [0]
    while positions[-1] < n:
        # Find the next position to move
        next_position = -1
        for i in range(len(platforms)):
            if platforms[i][0] <= positions[-1] and platforms[i][1] > positions[-1]:
                next_position = platforms[i][1]
                break
        if next_position == -1:
            return "NO"
        # Move the platform to the left or right
        platforms[0][0] = next_position
        platforms[0][1] -= 1
        platforms[-1][0] = next_position + 1
        platforms[-1][1] += 1
        positions.append(next_position)
    return "YES"

def get_platforms(n, m, c):
    platforms = []
    for i in range(m):
        platforms.append([i+1, c[i]])
    return platforms

def get_platforms_positions(platforms):
    positions = []
    for platform in platforms:
        positions.extend(list(range(platform[0], platform[0] + platform[1])))
    return positions

def get_answer(n, m, d, c):
    platforms = get_platforms(n, m, c)
    positions = get_platforms_positions(platforms)
    if positions[-1] != n:
        return "NO"
    answer = [0] * (n+2)
    for i in range(len(platforms)):
        for j in range(platforms[i][0], platforms[i][0] + platforms[i][1]):
            answer[j] = i+1
    return "YES", answer

if __name__ == '__main__':
    n, m, d = map(int, input().split())
    c = list(map(int, input().split()))
    print(get_answer(n, m, d, c))

