
def solve(n, a, b):
    # Find the largest number that is a multiple of 6 and less than or equal to n
    s = (n // 6) * 6
    
    # Calculate the final area of the room
    area = s * (a + b)
    
    # Return the final area and the new dimensions of the room
    return area, a + s, b + s

def main():
    n, a, b = map(int, input().split())
    area, a, b = solve(n, a, b)
    print(area)
    print(a, b)

if __name__ == '__main__':
    main()

