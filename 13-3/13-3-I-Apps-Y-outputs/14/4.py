
import math

def f1(A, B, C, D):
    # Calculate the vectors AB, BC, and CD
    AB = B - A
    BC = C - B
    CD = D - C
    
    # Calculate the cross product of AB and BC
    X = AB[0] * BC[1] - AB[1] * BC[0]
    Y = AB[0] * BC[2] - AB[2] * BC[0]
    Z = AB[1] * BC[2] - AB[2] * BC[1]
    
    # Calculate the dot product of X and Y
    XY = X * Y
    
    # Calculate the magnitude of X and Y
    X_mag = math.sqrt(X**2 + Y**2 + Z**2)
    Y_mag = math.sqrt(X**2 + Y**2 + Z**2)
    
    # Calculate the cosine of the angle between the plane and the line
    cos_phi = XY / (X_mag * Y_mag)
    
    # Calculate the angle in degrees
    phi = math.degrees(math.acos(cos_phi))
    
    return phi

def f2(...):
    # Your code here
    pass

if __name__ == '__main__':
    A = [float(x) for x in input().split()]
    B = [float(x) for x in input().split()]
    C = [float(x) for x in input().split()]
    D = [float(x) for x in input().split()]
    
    print(f1(A, B, C, D))

