
import math

def f1(A, B, C, D):
    # Calculate the vectors AB, BC, and CD
    AB = [B[0] - A[0], B[1] - A[1], B[2] - A[2]]
    BC = [C[0] - B[0], C[1] - B[1], C[2] - B[2]]
    CD = [D[0] - C[0], D[1] - C[1], D[2] - C[2]]

    # Calculate the dot product of AB and BC
    dot_product = AB[0] * BC[0] + AB[1] * BC[1] + AB[2] * BC[2]

    # Calculate the cross product of AB and BC
    cross_product = [AB[1] * BC[2] - AB[2] * BC[1], AB[2] * BC[0] - AB[0] * BC[2], AB[0] * BC[1] - AB[1] * BC[0]]

    # Calculate the magnitude of the cross product
    magnitude = math.sqrt(cross_product[0] ** 2 + cross_product[1] ** 2 + cross_product[2] ** 2)

    # Calculate the angle between the plane and the x-y plane
    angle = math.acos(dot_product / magnitude)

    # Return the angle in degrees
    return math.degrees(angle)

def f2(A, B, C, D):
    # Calculate the vectors AB, BC, and CD
    AB = [B[0] - A[0], B[1] - A[1], B[2] - A[2]]
    BC = [C[0] - B[0], C[1] - B[1], C[2] - B[2]]
    CD = [D[0] - C[0], D[1] - C[1], D[2] - C[2]]

    # Calculate the dot product of BC and CD
    dot_product = BC[0] * CD[0] + BC[1] * CD[1] + BC[2] * CD[2]

    # Calculate the cross product of BC and CD
    cross_product = [BC[1] * CD[2] - BC[2] * CD[1], BC[2] * CD[0] - BC[0] * CD[2], BC[0] * CD[1] - BC[1] * CD[0]]

    # Calculate the magnitude of the cross product
    magnitude = math.sqrt(cross_product[0] ** 2 + cross_product[1] ** 2 + cross_product[2] ** 2)

    # Calculate the angle between the plane and the x-y plane
    angle = math.acos(dot_product / magnitude)

    # Return the angle in degrees
    return math.degrees(angle)

if __name__ == '__main__':
    A = [float(x) for x in input().split()]
    B = [float(x) for x in input().split()]
    C = [float(x) for x in input().split()]
    D = [float(x) for x in input().split()]

    print(f1(A, B, C, D))
    print(f2(A, B, C, D))

