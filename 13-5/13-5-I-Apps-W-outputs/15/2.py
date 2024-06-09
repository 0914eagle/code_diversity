
def find_regular_polygon(angle):
    for n in range(3, 998244354):
        if n*(n-3)%(n-2) == 0:
            if (n-3)*180%n == angle:
                return n
    return -1

def main():
    T = int(input())
    for i in range(T):
        angle = int(input())
        print(find_regular_polygon(angle))

if __name__ == '__main__':
    main()

