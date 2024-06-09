
def get_designations(streets, properties):
    designations = []
    for property in properties:
        designation = "same"
        for street in streets:
            if street.intersects(property):
                designation = "different"
                break
        designations.append(designation)
    return designations

def main():
    streets_count = int(input())
    streets = []
    for _ in range(streets_count):
        x1, y1, x2, y2 = map(int, input().split())
        street = Line(x1, y1, x2, y2)
        streets.append(street)

    properties_count = int(input())
    properties = []
    for _ in range(properties_count):
        x3, y3, x4, y4 = map(int, input().split())
        property = Rectangle(x3, y3, x4, y4)
        properties.append(property)

    designations = get_designations(streets, properties)
    for designation in designations:
        print(designation)

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def intersects(self, rectangle):
        return self.intersects_x(rectangle) and self.intersects_y(rectangle)

    def intersects_x(self, rectangle):
        x_min = min(self.x1, self.x2)
        x_max = max(self.x1, self.x2)
        return x_min <= rectangle.x_max and rectangle.x_min <= x_max

    def intersects_y(self, rectangle):
        y_min = min(self.y1, self.y2)
        y_max = max(self.y1, self.y2)
        return y_min <= rectangle.y_max and rectangle.y_min <= y_max

class Rectangle:
    def __init__(self, x_min, y_min, x_max, y_max):
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max

if __name__ == '__main__':
    main()

