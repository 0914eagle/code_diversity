
def get_max_birds(length, distance, num_birds):
    available_space = length - num_birds * distance - 6
    return available_space // distance

