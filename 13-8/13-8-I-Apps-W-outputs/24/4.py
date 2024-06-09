
def find_solution(a, b, c):
    # Calculate the distances between the points
    ab_dist = ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5
    bc_dist = ((b[0]-c[0])**2 + (b[1]-c[1])**2)**0.5
    ca_dist = ((c[0]-a[0])**2 + (c[1]-a[1])**2)**0.5

    # Check if the distances are equal
    if ab_dist == bc_dist and bc_dist == ca_dist:
        return "Yes"
    else:
        return "No"

