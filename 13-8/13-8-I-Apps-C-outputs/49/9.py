
def pubnite(x_s, y_s, s_s, r_i, r_f, x_a, y_a, s_a):
    # Calculate the distance between Anthony's current position and the center of the safety zone
    distance = ((x_a - x_s) ** 2 + (y_a - y_s) ** 2) ** 0.5
    
    # Calculate the time it takes for Anthony to reach the center of the safety zone
    time = distance / s_a
    
    # Calculate the radius of the safety zone at the time Anthony reaches the center
    radius = r_i - s_s * time
    
    # Calculate the amount of damage Anthony will take if he stays in the safety zone until it shrinks to r_f
    damage = (radius ** 2 - r_f ** 2) / 2
    
    return damage

