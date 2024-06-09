
def find_minimum_spanning_tree(points):
    # Sort the points based on their x-coordinate
    sorted_points = sorted(points, key=lambda point: point[0])

    # Create a disjoint set to store the points and their parents
    dsu = DisjointSet(sorted_points)

    # Initialize the minimum spanning tree weight to 0
    mst_weight = 0

    # Iterate through the points and find the minimum spanning tree weight
    for i in range(len(sorted_points)):
        for j in range(i + 1, len(sorted_points)):
            # Calculate the Manhattan distance between the two points
            distance = abs(sorted_points[i][0] - sorted_points[j][0]) + abs(sorted_points[i][1] - sorted_points[j][1])

            # If the distance is less than or equal to the current minimum spanning tree weight, update the weight and merge the two points in the disjoint set
            if distance <= mst_weight:
                mst_weight = distance
                dsu.union(i, j)

    # Return the minimum spanning tree weight
    return mst_weight

# Define a class to represent a disjoint set
class DisjointSet:
    def __init__(self, points):
        self.parents = [-1] * len(points)
        self.ranks = [0] * len(points)
        self.size = len(points)

    # Find the root of the tree
    def find(self, point):
        if self.parents[point] == -1:
            return point
        else:
            self.parents[point] = self.find(self.parents[point])
            return self.parents[point]

    # Union two points in the disjoint set
    def union(self, point1, point2):
        root1 = self.find(point1)
        root2 = self.find(point2)

        # If the roots are not the same, combine them
        if root1 != root2:
            if self.ranks[root1] > self.ranks[root2]:
                self.parents[root2] = root1
            else:
                self.parents[root1] = root2
                if self.ranks[root1] == self.ranks[root2]:
                    self.ranks[root2] += 1
            self.size -= 1

    # Return the size of the disjoint set
    def get_size(self):
        return self.size

