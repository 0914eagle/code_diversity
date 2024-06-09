
def get_min_damage(x_s, y_s, s_s, r_i, r_f, x_a, y_a, s_a):
    # Calculate the distance between Anthony's current position and the center of the safety zone
    dist = ((x_a - x_s) ** 2 + (y_a - y_s) ** 2) ** 0.5
    
    # Calculate the time it takes for Anthony to reach the safety zone
    time = dist / s_a
    
    # Calculate the amount of damage Anthony will take during this time
    damage = time * s_s
    
    # If the safety zone has already shrunk to a radius of r_f, return the damage
    if r_i <= r_f:
        return damage
    
    # Calculate the radius of the safety zone at the time Anthony reaches it
    radius = r_i - time * s_s
    
    # If the safety zone has already shrunk to a radius of r_f, return the damage
    if radius <= r_f:
        return damage
    
    # Calculate the amount of damage Anthony will take after reaching the safety zone
    damage += (radius - r_f) * s_s
    
    return damage

