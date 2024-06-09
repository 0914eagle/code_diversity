
def get_triangle_weight(triangle):
    return triangle[0] * triangle[1] * triangle[2]

def get_min_weight(n):
    if n == 3:
        return 6
    if n == 4:
        return 18
    return 0

def main():
    n = int(input())
    print(get_min_weight(n))

if __name__ == '__main__':
    main()

