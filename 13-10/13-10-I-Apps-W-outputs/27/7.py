
def get_boring_pairs(planets, paths):
    boring_pairs = set()
    for i in range(len(paths)):
        for j in range(i + 1, len(paths)):
            if paths[i][2] ^ paths[j][2] == 0 and (paths[i][0], paths[j][1]) not in boring_pairs and (paths[j][0], paths[i][1]) not in boring_pairs:
                boring_pairs.add((paths[i][0], paths[j][1]))
                boring_pairs.add((paths[j][0], paths[i][1]))
    return boring_pairs

def get_number_of_boring_pairs(planets, paths, order):
    boring_pairs = get_boring_pairs(planets, paths)
    number_of_boring_pairs = 0
    for i in range(len(order)):
        path = (paths[order[i] - 1][0], paths[order[i] - 1][1])
        if path in boring_pairs:
            boring_pairs.remove(path)
            number_of_boring_pairs += 1
    return number_of_boring_pairs

def main():
    planets = int(input())
    paths = []
    for i in range(planets - 1):
        paths.append(list(map(int, input().split())))
    order = list(map(int, input().split()))
    for i in range(planets):
        print(get_number_of_boring_pairs(planets, paths, order[:i + 1]))

if __name__ == '__main__':
    main()

