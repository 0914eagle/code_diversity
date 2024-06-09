
def is_solvable(a, b, c):
    # Calculate the dot product of the vectors ab and ac
    dot_product = (b[0] - a[0]) * (c[0] - a[0]) + (b[1] - a[1]) * (c[1] - a[1])
    
    # Calculate the magnitude of the vectors ab and ac
    ab_mag = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5
    ac_mag = ((c[0] - a[0]) ** 2 + (c[1] - a[1]) ** 2) ** 0.5
    
    # Check if the dot product is equal to the product of the magnitudes
    if dot_product == ab_mag * ac_mag:
        return True
    else:
        return False

