
def count_triangles(sides):
    # Calculate the perimeter of the hexagon
    perimeter = sum(sides)
    # Calculate the number of triangles
    num_triangles = perimeter * 2 - 3
    return num_triangles

if __name__ == '__main__':
    sides = list(map(int, input().split()))
    print(count_triangles(sides))

