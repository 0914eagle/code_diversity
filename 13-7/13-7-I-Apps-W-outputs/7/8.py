
def is_regular_polygon(a):
    return a in [30, 60, 90]

def main():
    tests = int(input())
    for _ in range(tests):
        a = int(input())
        if is_regular_polygon(a):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()

