
def read_input():
    n = int(input())
    fruits = []
    for _ in range(n):
        x, y = map(float, input().split())
        fruits.append((x, y))
    return n, fruits

def find_max_sliced_fruits(fruits):
    # find the line that passes through the center of the fruits
    x_center = sum(x for x, y in fruits) / len(fruits)
    y_center = sum(y for x, y in fruits) / len(fruits)
    line_slope = (y_center - fruits[0][1]) / (x_center - fruits[0][0])
    line_intercept = y_center - line_slope * x_center

    # find the maximum number of fruits that can be sliced with this line
    max_sliced_fruits = 0
    for fruit in fruits:
        fruit_center_x = fruit[0]
        fruit_center_y = fruit[1]
        distance_from_line = abs(line_slope * fruit_center_x - fruit_center_y + line_intercept)
        if distance_from_line <= 1:
            max_sliced_fruits += 1

    return max_sliced_fruits

def main():
    n, fruits = read_input()
    print(find_max_sliced_fruits(fruits))

if __name__ == '__main__':
    main()

