
def get_input():
    n = int(input())
    fruits = []
    for _ in range(n):
        x, y = map(float, input().split())
        fruits.append((x, y))
    return n, fruits

def get_slices(fruits):
    slices = []
    for i in range(len(fruits)):
        for j in range(i+1, len(fruits)):
            slice = get_slice(fruits[i], fruits[j])
            if slice not in slices:
                slices.append(slice)
    return slices

def get_slice(fruit1, fruit2):
    x1, y1 = fruit1
    x2, y2 = fruit2
    return (x1, y1, x2, y2)

def get_intersection(slice1, slice2):
    x1, y1, x2, y2 = slice1
    x3, y3, x4, y4 = slice2
    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if denom == 0:
        return None
    x = (x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)
    y = (x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)
    return x / denom, y / denom

def get_fruits_in_slice(slice, fruits):
    fruits_in_slice = []
    for fruit in fruits:
        if get_intersection(slice, get_slice(fruit, (0, 0))) is not None:
            fruits_in_slice.append(fruit)
    return fruits_in_slice

def get_max_fruits(slices, fruits):
    max_fruits = 0
    for slice in slices:
        fruits_in_slice = get_fruits_in_slice(slice, fruits)
        if len(fruits_in_slice) > max_fruits:
            max_fruits = len(fruits_in_slice)
    return max_fruits

def main():
    n, fruits = get_input()
    slices = get_slices(fruits)
    max_fruits = get_max_fruits(slices, fruits)
    print(max_fruits)

if __name__ == '__main__':
    main()

