
def get_max_distance(n, x, a, b):
    if a == b:
        return 0
    
    distance = abs(a - b)
    if x == 0:
        return distance
    
    if a < b:
        a, b = b, a
    
    for i in range(a-1, b):
        distance = max(distance, abs(i - b))
    
    for i in range(b+1, a):
        distance = max(distance, abs(i - a))
    
    return distance

def main():
    t = int(input())
    for _ in range(t):
        n, x, a, b = map(int, input().split())
        print(get_max_distance(n, x, a, b))

if __name__ == '__main__':
    main()

