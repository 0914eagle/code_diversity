
def get_corner_pairs(n):
    corner_pairs = []
    for i in range(n):
        r, c = map(int, input().split())
        corner_pairs.append((r, c))
    return corner_pairs

def get_matching(corner_pairs):
    n = len(corner_pairs)
    matching = [0] * n
    for i in range(n):
        for j in range(i+1, n):
            if is_match(corner_pairs[i], corner_pairs[j]):
                matching[i] = j
                matching[j] = i
                break
    
    for i in range(n):
        if matching[i] == 0:
            return "syntax error"
    
    return matching

def is_match(corner1, corner2):
    r1, c1 = corner1
    r2, c2 = corner2
    return r1 == r2 or c1 == c2 or r1 == c2 or r2 == c1

def main():
    n = int(input())
    corner_pairs = get_corner_pairs(n)
    matching = get_matching(corner_pairs)
    print(*matching)

if __name__ == '__main__':
    main()

