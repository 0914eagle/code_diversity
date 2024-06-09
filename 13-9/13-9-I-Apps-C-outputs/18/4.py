
def get_largest_corn_area(polygon, canal):
    
    # Convert the polygon and canal to shapely objects
    polygon = shapely.geometry.Polygon(polygon)
    canal = shapely.geometry.LineString(canal)

    # Create a copy of the polygon to work with
    polygon_copy = polygon.copy()

    # Iterate through the vertices of the polygon
    for vertex in polygon.exterior.coords:
        # Check if the vertex is on the right side of the canal
        if shapely.geometry.LineString([vertex, canal.interpolate(0.5)]).distance(canal) < 0:
            # If it is, remove the corresponding triangle from the polygon
            polygon_copy = polygon_copy.difference(shapely.geometry.Polygon([vertex, canal.interpolate(0.5), canal.interpolate(1)]))

    # Return the area of the largest triangle
    return max(polygon_copy.difference(canal).area, key=abs)

