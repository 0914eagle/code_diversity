
def find_celery(vertices, sightings):
    # Step 1: Find the convex hull of the sightings
    from scipy.spatial import ConvexHull
    hull = ConvexHull(sightings)
    
    # Step 2: Find the intersection of the convex hull with the Alexa Forest polygon
    from shapely.geometry import Polygon, MultiPoint
    polygon = Polygon(vertices)
    hull_points = MultiPoint(hull.points[hull.vertices])
    intersection = polygon.intersection(hull_points)
    
    # Step 3: Return the number of vertices of the intersection polygon
    return len(intersection.exterior.coords)

