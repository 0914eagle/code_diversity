
def get_perimeter(a, b):
    perimeter = 2 * (a + b)
    return perimeter

def main():
    a, b = map(int, input().split())
    perimeter = get_perimeter(a, b)
    print(perimeter)

if __name__ == '__main__':
    main()

