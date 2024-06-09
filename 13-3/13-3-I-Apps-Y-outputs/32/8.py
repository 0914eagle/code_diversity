
def check_template_containment(image_a, template_image):
    # Initialize a flag to keep track of whether the template image is contained in the image A
    contained = True
    
    # Loop through each row of the template image
    for i in range(len(template_image)):
        # Loop through each column of the template image
        for j in range(len(template_image[0])):
            # Check if the pixel at the current position in the template image matches the pixel at the same position in the image A
            if template_image[i][j] != image_a[i][j]:
                # If the pixels do not match, set the contained flag to False and break out of the loops
                contained = False
                break
        # If the contained flag is False, break out of the loops
        if not contained:
            break
    
    # Return the contained flag
    return contained

def main():
    # Read the input data from stdin
    image_a_size, template_image_size = map(int, input().split())
    image_a = [input() for _ in range(image_a_size)]
    template_image = [input() for _ in range(template_image_size)]
    
    # Check if the template image is contained in the image A
    contained = check_template_containment(image_a, template_image)
    
    # Print the result
    print("Yes" if contained else "No")

if __name__ == '__main__':
    main()

