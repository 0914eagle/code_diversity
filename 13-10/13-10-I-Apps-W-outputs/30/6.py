
def get_rectangles(r, c, x, y):
    
    rectangles = []
    
    # Add the viola's row
    rectangles.append([[x, 1], [x, c]])
    
    # Add the viola's column
    rectangles.append([[1, y], [r, y]])
    
    # Add the entire string section
    rectangles.append([[1, 1], [r, c]])
    
    return rectangles

def count_violas(rectangles, violas):
    
    count = 0
    for rectangle in rectangles:
        for viola in violas:
            if rectangle[0][0] <= viola[0] <= rectangle[1][0] and rectangle[0][1] <= viola[1] <= rectangle[1][1]:
                count += 1
    return count

def main():
    r, c, n, k = map(int, input().split())
    violas = []
    for _ in range(n):
        violas.append(list(map(int, input().split())))
    
    rectangles = get_rectangles(r, c, violas[0][0], violas[0][1])
    count = count_violas(rectangles, violas)
    
    print(count)

if __name__ == '__main__':
    main()

