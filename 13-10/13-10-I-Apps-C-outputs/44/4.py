
def is_similar(world1, world2):
    # Check if the vertex sets of the two worlds are the same
    if world1.V != world2.V:
        return False
    
    # Check if the edge sets of the two worlds are the same
    if world1.E != world2.E:
        return False
    
    # Check if the s and t vertices are the same
    if world1.s != world2.s or world1.t != world2.t:
        return False
    
    return True

def count_similar_worlds(worlds):
    # Initialize a set to store the non-similar worlds
    non_similar_worlds = set()
    
    # Iterate over the worlds
    for world in worlds:
        # Check if the current world is already in the set of non-similar worlds
        if world not in non_similar_worlds:
            # If not, add it to the set and check if it is similar to any of the other worlds
            non_similar_worlds.add(world)
            for other_world in non_similar_worlds:
                if is_similar(world, other_world):
                    # If it is similar, merge the two worlds into one
                    non_similar_worlds.remove(other_world)
                    non_similar_worlds.add(world.merge(other_world))
                    break
    
    # Return the number of non-similar worlds
    return len(non_similar_worlds)

def main():
    # Read the input
    n, m = map(int, input().split())
    
    # Initialize the first world with two vertices and an edge between them
    world = World(2)
    world.add_edge(0, 1)
    
    # Perform the specified number of changes
    for _ in range(n):
        world.add_vertex()
        for edge in world.edges:
            world.add_edge(edge[0], edge[1], edge[2])
    
    # Find the non-similar worlds
    non_similar_worlds = count_similar_worlds(world)
    
    # Print the number of non-similar worlds
    print(non_similar_worlds)

class World:
    def __init__(self, n):
        self.V = set(range(n))
        self.E = set()
        self.s = 0
        self.t = 1
    
    def add_vertex(self):
        self.V.add(len(self.V))
    
    def add_edge(self, u, v, w=None):
        if w is None:
            w = len(self.V)
        self.E.add((u, v, w))
    
    def merge(self, other):
        world = World(len(self.V) + len(other.V) - 2)
        world.V = self.V | other.V - {self.s, self.t, other.s, other.t}
        world.E = self.E | other.E
        return world

if __name__ == '__main__':
    main()

