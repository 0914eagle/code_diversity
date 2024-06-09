
import math

def get_fruits_coordinates(n):
    fruits = []
    for i in range(n):
        x, y = map(float, input().split())
        fruits.append((x, y))
    return fruits

def get_max_fruits_sliced(fruits):
    max_fruits_sliced = 0
    for i in range(len(fruits)):
        for j in range(i+1, len(fruits)):
            fruit1, fruit2 = fruits[i], fruits[j]
            distance = math.sqrt((fruit1[0]-fruit2[0])**2 + (fruit1[1]-fruit2[1])**2)
            if distance <= 2:
                max_fruits_sliced += 1
    return max_fruits_sliced

def main():
    n = int(input())
    fruits = get_fruits_coordinates(n)
    max_fruits_sliced = get_max_fruits_sliced(fruits)
    print(max_fruits_sliced)

if __name__ == '__main__':
    main()

