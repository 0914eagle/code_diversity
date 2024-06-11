def triangle_area(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.
    Example:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1
    '''
    # Write your code here.
    if a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2
        return round(s * (s - a) * (s - b) * (s - c), 2)
    else:
        return -1

print(triangle_area(3, 4, 5))
print(triangle_area(1, 2, 10))
print(triangle_area(1, 2, 3))
print(triangle_area(1, 2, 4))
print(triangle_area(1, 2, 5))
print(triangle_area(1, 2, 6))
print(triangle_area(1, 2, 7))
print(triangle_area(1, 2, 8))
print(triangle_area(1, 2, 9))
print(triangle_area(1, 2, 10))
print(triangle_area(1, 2, 11))
print(triangle_area(1, 2, 12))
print(triangle_area(1, 2, 13))
print(triangle_area(1, 2, 14))
print(triangle_area(1, 2, 15))
print(triangle_area(1, 2, 16))
print(triangle_area(1, 2, 17))
print(triangle_area(1, 2, 18))
print(triangle_area(1, 2, 19))
print(triangle_area(1, 2, 20))
print(triangle_area(1, 2, 21))
print(triangle_area(1, 2, 22))
print(triangle_area(1, 2, 23))
print(triangle_area(1, 2, 24))
print(triangle_area(1, 2, 25))
print(triangle_area(1, 2, 26))
print(triangle_area(1, 2, 27))
print(triangle_area(1, 2, 2