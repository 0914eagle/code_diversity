
def solve(n, a):
    # Initialize the number of components to 0
    num_components = 0

    # Iterate over the range of values from 1 to n
    for l in range(1, n + 1):
        # Initialize the current component to 0
        current_component = 0

        # Iterate over the range of values from l to n
        for r in range(l, n + 1):
            # Initialize the number of vertices to 0
            num_vertices = 0

            # Iterate over the input array
            for i in range(n):
                # Check if the current value is between l and r (inclusive)
                if l <= a[i] <= r:
                    # Increment the number of vertices
                    num_vertices += 1

            # Check if the number of vertices is greater than 0
            if num_vertices > 0:
                # Increment the current component
                current_component += 1

        # Add the current component to the total number of components
        num_components += current_component

    # Return the total number of components
    return num_components

