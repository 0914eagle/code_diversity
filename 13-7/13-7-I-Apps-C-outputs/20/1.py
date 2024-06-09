
def solve(P, A, pine_locations, aspen_locations):
    # Calculate the area covered by both species
    area = 0
    
    # Iterate over each pine tree
    for pine in pine_locations:
        # Find the aspens that are within range of the pine tree
        aspens_in_range = []
        for aspen in aspen_locations:
            if (pine[0] - aspen[0]) ** 2 + (pine[1] - aspen[1]) ** 2 <= 1:
                aspens_in_range.append(aspen)
        
        # Calculate the area of the triangle formed by the pine tree and the aspens in range
        for i in range(len(aspens_in_range)):
            for j in range(i+1, len(aspens_in_range)):
                area += triangle_area(pine, aspens_in_range[i], aspens_in_range[j])
    
    return area

def triangle_area(a, b, c):
    # Calculate the area of a triangle using Heron's formula
    s = (a[0] - c[0]) ** 2 + (a[1] - c[1]) ** 2
    area = 0.5 * (-s * (s - (a[0] - b[0]) ** 2) * (s - (a[1] - b[1]) ** 2) * (s - (c[0] - b[0]) ** 2) * (s - (c[1] - b[1]) ** 2)) ** 0.5
    return area

