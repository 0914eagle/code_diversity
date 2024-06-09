
def f1(n, pebbles):
    # find the pairs of pebbles where Yoshi can perform a jump
    pairs = []
    for i in range(n-1):
        for j in range(i+1, n):
            if pebbles[i] + pebbles[j] == j - i:
                pairs.append((i, j))
    
    # find the most distant pebble that can be reached
    max_dist = 0
    for i in range(n):
        for j in range(i+1, n+1):
            if all(k not in pairs for k in range(i, j)):
                max_dist = max(max_dist, j-i)
    
    return max_dist

def f2(n, pebbles):
    # find the pairs of pebbles where Yoshi can perform a jump
    pairs = []
    for i in range(n-1):
        for j in range(i+1, n):
            if pebbles[i] + pebbles[j] == j - i:
                pairs.append((i, j))
    
    # find the most distant pebble that can be reached
    max_dist = 0
    for i in range(n):
        for j in range(i+1, n+1):
            if all(k not in pairs for k in range(i, j)):
                max_dist = max(max_dist, j-i)
    
    return max_dist

if __name__ == '__main__':
    n = int(input())
    pebbles = list(map(int, input().split()))
    print(f1(n, pebbles))
    print(f2(n, pebbles))

