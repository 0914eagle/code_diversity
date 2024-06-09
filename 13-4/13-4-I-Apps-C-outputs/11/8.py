
import math

def get_input():
    n = int(input())
    fruits = []
    for i in range(n):
        x, y = map(float, input().split())
        fruits.append((x, y))
    return n, fruits

def get_max_sliced_fruits(fruits):
    max_sliced_fruits = 0
    for i in range(len(fruits)):
        for j in range(i+1, len(fruits)):
            if fruits[i][1] == fruits[j][1]:
                continue
            slope = (fruits[j][1] - fruits[i][1]) / (fruits[j][0] - fruits[i][0])
            y_intercept = fruits[i][1] - slope * fruits[i][0]
            x_intercept = -y_intercept / slope
            if x_intercept >= min(fruits[i][0], fruits[j][0]) and x_intercept <= max(fruits[i][0], fruits[j][0]):
                max_sliced_fruits += 1
    return max_sliced_fruits

def main():
    n, fruits = get_input()
    print(get_max_sliced_fruits(fruits))

if __name__ == '__main__':
    main()

