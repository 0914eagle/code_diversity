
def calculate_angle(A, B, C, D):
    AB = B - A
    BC = C - B
    CD = D - C
    X = np.cross(AB, BC)
    Y = np.cross(BC, CD)
    cos_phi = np.dot(X, Y)/(np.linalg.norm(X)*np.linalg.norm(Y))
    phi = np.arccos(cos_phi)
    return np.rad2deg(phi)

def input_data():
    A = input("Enter the coordinates of point A: ").split()
    B = input("Enter the coordinates of point B: ").split()
    C = input("Enter the coordinates of point C: ").split()
    D = input("Enter the coordinates of point D: ").split()
    return A, B, C, D

if __name__ == '__main__':
    A, B, C, D = input_data()
    angle = calculate_angle(A, B, C, D)
    print(f"The angle between the plane made by points A, B, C and points B, C, D is {angle:.2f} degrees.")

