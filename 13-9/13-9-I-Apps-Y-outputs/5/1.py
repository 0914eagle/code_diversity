
def get_input():
    W, H = map(int, input().split())
    assert 3 <= W <= 50 and 3 <= H <= 50
    map = []
    for _ in range(H):
        map.append(list(input()))
    return W, H, map

def get_safe_gold(W, H, map):
    safe_gold = 0
    for i in range(H):
        for j in range(W):
            if map[i][j] == 'G':
                safe_gold += 1
    return safe_gold

def main():
    W, H, map = get_input()
    safe_gold = get_safe_gold(W, H, map)
    print(safe_gold)

if __name__ == '__main__':
    main()

