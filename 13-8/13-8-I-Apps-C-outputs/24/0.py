
def minimum_spanning_tree(points):
    # Sort the points based on their x-coordinate
    sorted_points = sorted(points, key=lambda point: point[0])

    # Create a disjoint set to store the connected components
    disjoint_set = DisjointSet()

    # Initialize the total weight of the MST to 0
    total_weight = 0

    # Iterate through the sorted points
    for i in range(len(sorted_points)):
        # Get the current point and its x-coordinate
        current_point = sorted_points[i]
        current_x = current_point[0]

        # Find the nearest point to the current point in the disjoint set
        nearest_point = disjoint_set.find_nearest(current_point)

        # If the nearest point is not None, add the weight of the edge to the total weight
        if nearest_point is not None:
            total_weight += manhattan_distance(current_point, nearest_point)

        # Add the current point to the disjoint set
        disjoint_set.add(current_point)

    return total_weight

def manhattan_distance(point1, point2):
    # Return the Manhattan distance between the two points
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

class DisjointSet:
    def __init__(self):
        self.parents = {}
        self.ranks = {}

    def find_nearest(self, point):
        # Find the nearest point in the disjoint set
        nearest_point = None
        min_distance = float('inf')
        for current_point in self.parents:
            distance = manhattan_distance(point, current_point)
            if distance < min_distance:
                min_distance = distance
                nearest_point = current_point
        return nearest_point

    def add(self, point):
        # Add the point to the disjoint set
        self.parents[point] = point
        self.ranks[point] = 0

