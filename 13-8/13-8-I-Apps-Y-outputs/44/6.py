
def get_platforms_lengths(m):
    return list(map(int, input().split()))

def get_platforms_positions(n, m, c):
    platforms = []
    current_position = 0
    for i in range(m):
        platforms.append([current_position, current_position + c[i] - 1])
        current_position += c[i]
    return platforms

def can_reach_end(n, m, d, c):
    platforms = get_platforms_positions(n, m, c)
    current_position = 0
    for i in range(m):
        if current_position in platforms[i]:
            current_position = platforms[i][1]
        else:
            current_position += d
            if current_position > n:
                return False
    return True

def get_platforms_sequence(n, m, c):
    platforms = get_platforms_positions(n, m, c)
    sequence = [0] * (n + 2)
    for i in range(m):
        for j in range(platforms[i][0], platforms[i][1] + 1):
            sequence[j] = i + 1
    return sequence

def main():
    n, m, d = map(int, input().split())
    c = get_platforms_lengths(m)
    if can_reach_end(n, m, d, c):
        print("YES")
        print(" ".join(map(str, get_platforms_sequence(n, m, c))))
    else:
        print("NO")

if __name__ == '__main__':
    main()

