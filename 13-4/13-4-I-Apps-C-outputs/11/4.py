
def get_input():
    n = int(input())
    fruits = []
    for i in range(n):
        x, y = map(float, input().split())
        fruits.append((x, y))
    return n, fruits

def get_max_sliced_fruits(fruits):
    # Find the line that passes through the center of the fruits
    center_x = sum(x for x, _ in fruits) / len(fruits)
    center_y = sum(y for _, y in fruits) / len(fruits)
    line_slope = (center_y - fruits[0][1]) / (center_x - fruits[0][0])
    line_intercept = fruits[0][1] - line_slope * fruits[0][0]

    # Find the maximum number of fruits that can be sliced with this line
    max_sliced_fruits = 0
    for fruit in fruits:
        fruit_center_x = (fruit[0] + fruit[1]) / 2
        fruit_center_y = (fruit[0] + fruit[1]) / 2
        distance_from_line = abs(line_slope * fruit_center_x - fruit_center_y + line_intercept) / math.sqrt(1 + line_slope ** 2)
        if distance_from_line <= 1:
            max_sliced_fruits += 1

    return max_sliced_fruits

def main():
    n, fruits = get_input()
    print(get_max_sliced_fruits(fruits))

if __name__ == '__main__':
    main()

