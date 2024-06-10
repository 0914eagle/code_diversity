
def get_cost(rectangle):
    
    w, h = rectangle[2] - rectangle[0] + 1, rectangle[3] - rectangle[1] + 1
    return min(w, h)


def get_optimal_solution(rectangles):
    
    # Sort the rectangles by their areas in descending order
    rectangles.sort(key=lambda x: (x[2] - x[0] + 1) * (x[3] - x[1] + 1), reverse=True)

    # Initialize the optimal solution with the first rectangle
    solution = [rectangles[0]]

    # Iterate through the remaining rectangles
    for rectangle in rectangles[1:]:
        # Check if the rectangle intersects with any of the rectangles in the solution
        intersects = False
        for sol_rect in solution:
            if do_intersect(rectangle, sol_rect):
                intersects = True
                break

        # If the rectangle does not intersect with any of the rectangles in the solution, add it to the solution
        if not intersects:
            solution.append(rectangle)

    # Calculate the total cost of the optimal solution
    total_cost = sum(get_cost(rectangle) for rectangle in solution)

    return total_cost


def do_intersect(rect1, rect2):
    
    x1, y1, x2, y2 = rect1
    x3, y3, x4, y4 = rect2
    return not (x3 >= x2 or x4 <= x1 or y3 >= y2 or y4 <= y1)


def main():
    n, m = map(int, input().split())
    rectangles = []
    for _ in range(m):
        x1, y1, x2, y2 = map(int, input().split())
        rectangles.append([x1, y1, x2, y2])
    print(get_optimal_solution(rectangles))


if __name__ == '__main__':
    main()

