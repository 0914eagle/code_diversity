
import math

def get_arrow_points(px, py, vx, vy, a, b, c, d):
    # Calculate the length of the arrow
    arrow_length = math.sqrt(vx**2 + vy**2)
    
    # Calculate the angle of the arrow
    arrow_angle = math.atan2(vy, vx)
    
    # Calculate the coordinates of the tip of the arrow
    tip_x = px + arrow_length * math.cos(arrow_angle)
    tip_y = py + arrow_length * math.sin(arrow_angle)
    
    # Calculate the coordinates of the base of the arrow
    base_x = px - arrow_length * math.cos(arrow_angle)
    base_y = py - arrow_length * math.sin(arrow_angle)
    
    # Calculate the coordinates of the points on the base of the arrow
    point1_x = base_x + a * math.cos(arrow_angle)
    point1_y = base_y + a * math.sin(arrow_angle)
    point2_x = base_x - a * math.cos(arrow_angle)
    point2_y = base_y - a * math.sin(arrow_angle)
    
    # Calculate the coordinates of the points on the side of the arrow
    point3_x = point1_x + b * math.sin(arrow_angle)
    point3_y = point1_y - b * math.cos(arrow_angle)
    point4_x = point2_x + b * math.sin(arrow_angle)
    point4_y = point2_y - b * math.cos(arrow_angle)
    
    # Calculate the coordinates of the points on the rectangle
    point5_x = point3_x + c * math.cos(arrow_angle)
    point5_y = point3_y + c * math.sin(arrow_angle)
    point6_x = point4_x + c * math.cos(arrow_angle)
    point6_y = point4_y + c * math.sin(arrow_angle)
    point7_x = point5_x + d * math.sin(arrow_angle)
    point7_y = point5_y - d * math.cos(arrow_angle)
    point8_x = point6_x + d * math.sin(arrow_angle)
    point8_y = point6_y - d * math.cos(arrow_angle)
    
    # Return the coordinates of the arrow points in counter-clockwise order
    return [tip_x, tip_y, point1_x, point1_y, point2_x, point2_y, point3_x, point3_y, point4_x, point4_y, point5_x, point5_y, point6_x, point6_y, point7_x, point7_y, point8_x, point8_y]

def main():
    px, py, vx, vy, a, b, c, d = map(int, input().split())
    points = get_arrow_points(px, py, vx, vy, a, b, c, d)
    for point in points:
        print(point[0], point[1])

if __name__ == '__main__':
    main()

