
def count_faces(image):
    # Initialize a counter for the number of faces
    face_count = 0
    
    # Loop through the image and check for faces
    for i in range(len(image) - 1):
        for j in range(len(image[i]) - 1):
            # Check if the current square contains the letters "face"
            if image[i][j] == "f" and image[i][j + 1] == "a" and image[i + 1][j] == "c" and image[i + 1][j + 1] == "e":
                face_count += 1
    
    return face_count

