
def get_possible_x(y, k, n):
    # Find all possible values of x that satisfy the conditions
    possible_x = []
    for x in range(1, n//k+1):
        if (x+y)%k == 0 and x+y <= n:
            possible_x.append(x)
    
    # Sort and return the possible values of x
    possible_x.sort()
    return possible_x

def main():
    y, k, n = map(int, input().split())
    possible_x = get_possible_x(y, k, n)
    if possible_x:
        print(*possible_x)
    else:
        print(-1)

if __name__ == '__main__':
    main()

