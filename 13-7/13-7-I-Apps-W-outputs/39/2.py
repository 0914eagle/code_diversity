
def get_prefix_rectangles(feature):
    prefix_rectangles = []
    for i in range(len(feature)):
        for j in range(len(feature[0])):
            if feature[i][j] == "W":
                prefix_rectangles.append((i, j, 1))
            elif feature[i][j] == "B":
                prefix_rectangles.append((i, j, -1))
    return prefix_rectangles

def calculate_minimum_operations(prefix_rectangles):
    minimum_operations = 0
    for prefix_rectangle in prefix_rectangles:
        i, j, coefficient = prefix_rectangle
        minimum_operations += coefficient * (i + 1)
    return minimum_operations

def main():
    n, m = map(int, input().split())
    feature = []
    for i in range(n):
        feature.append(list(input()))
    prefix_rectangles = get_prefix_rectangles(feature)
    minimum_operations = calculate_minimum_operations(prefix_rectangles)
    print(minimum_operations)

if __name__ == '__main__':
    main()

