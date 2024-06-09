
def get_cube_vertices(coordinates):
    # Sort the coordinates
    coordinates = sorted(coordinates)
    
    # Get the unique coordinates
    unique_coordinates = list(set(coordinates))
    
    # Check if the coordinates form a cube
    if len(unique_coordinates) == 8:
        return unique_coordinates
    else:
        return None

def restore_cube_vertices(coordinates):
    # Get the cube vertices
    cube_vertices = get_cube_vertices(coordinates)
    
    # Check if the cube vertices are valid
    if cube_vertices is not None:
        return cube_vertices
    else:
        return "NO"

if __name__ == '__main__':
    coordinates = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1], [0, 1, 1]]
    print(restore_cube_vertices(coordinates))

