
def find_substring(s, t):
    n = len(s)
    m = len(t)
    if n > m:
        return -1
    
    count = 0
    for i in range(n):
        if s[i] != t[i]:
            count += 1
    
    return count

def find_substring_position(s, t):
    n = len(s)
    m = len(t)
    if n > m:
        return []
    
    positions = []
    for i in range(n):
        if s[i] != t[i]:
            positions.append(i+1)
    
    return positions

def main():
    n, m = map(int, input().split())
    s = input()
    t = input()
    
    count = find_substring(s, t)
    positions = find_substring_position(s, t)
    
    print(count)
    for position in positions:
        print(position, end=" ")

if __name__ == '__main__':
    main()

