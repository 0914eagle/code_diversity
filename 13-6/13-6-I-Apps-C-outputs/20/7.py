
def input_data():
    data = []
    for i in range(6):
        line = input()
        data.append(line)
    return data

def is_connected(data):
    visited = set()
    queue = []
    for i in range(6):
        for j in range(6):
            if data[i][j] == '#':
                queue.append((i, j))
                visited.add((i, j))
                break
    while queue:
        i, j = queue.pop(0)
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < 6 and 0 <= nj < 6 and (ni, nj) not in visited and data[ni][nj] == '#':
                queue.append((ni, nj))
                visited.add((ni, nj))
    return len(visited) == 6

def is_cube(data):
    for i in range(6):
        for j in range(6):
            if data[i][j] == '#':
                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < 6 and 0 <= nj < 6 and data[ni][nj] == '#':
                        data[i][j] = '.'
                        data[ni][nj] = '.'
                        if is_cube(data):
                            return True
                        data[i][j] = '#'
                        data[ni][nj] = '#'
    return False

def main():
    data = input_data()
    if is_connected(data) and is_cube(data):
        print("can fold")
    else:
        print("cannot fold")

if __name__ == '__main__':
    main()

