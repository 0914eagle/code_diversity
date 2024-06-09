
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
        x3, y3, x4, y4 = rectangle.x1, rectangle.y1, rectangle.x2, rectangle.y2
        return self.intersects_segment(x3, y3, x4, y4)

    def intersects_segment(self, x3, y3, x4, y4):
        denom = (self.y2 - self.y1) * (x4 - x3) - (self.x2 - self.x1) * (y4 - y3)
        if denom == 0:
            return False
        ua = ((x3 - self.x1) * (self.y2 - self.y1) - (self.y3 - self.y1) * (x4 - self.x1)) / denom
        ub = ((x3 - self.x1) * (y4 - self.y1) - (self.y3 - self.y1) * (x4 - self.x1)) / denom
        return 0 <= ua <= 1 and 0 <= ub <= 1

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def intersects(self, line):
        return line.intersects(self)

if __name__ == '__main__':
    main()

