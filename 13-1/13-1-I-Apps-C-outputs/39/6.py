
def get_total_distance(adil_x, adil_y, bera_x, bera_y, recycling_bin_x, recycling_bin_y, bottles):
    
    # Calculate the distance from Adil's and Bera's initial position to the recycling bin
    adil_distance = get_distance(adil_x, adil_y, recycling_bin_x, recycling_bin_y)
    bera_distance = get_distance(bera_x, bera_y, recycling_bin_x, recycling_bin_y)

    # Initialize the minimum total distance to the maximum possible value
    min_total_distance = float('inf')

    # Iterate over all possible combinations of bottles that Adil and Bera can pick
    for adil_bottles, bera_bottles in itertools.combinations(bottles, len(bottles)):
        # Calculate the total distance that Adil and Bera need to walk for this combination of bottles
        adil_path = get_path(adil_x, adil_y, adil_bottles)
        bera_path = get_path(bera_x, bera_y, bera_bottles)
        total_distance = adil_distance + bera_distance + sum(adil_path + bera_path)

        # Update the minimum total distance if necessary
        if total_distance < min_total_distance:
            min_total_distance = total_distance

    return min_total_distance

def get_distance(x1, y1, x2, y2):
    
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def get_path(x, y, bottles):
    
    path = []
    for bottle in bottles:
        path.append(get_distance(x, y, bottle[0], bottle[1]))
        x, y = bottle[0], bottle[1]
    return path

if __name__ == '__main__':
    adil_x, adil_y, bera_x, bera_y, recycling_bin_x, recycling_bin_y = map(int, input().split())
    n = int(input())
    bottles = []
    for _ in range(n):
        x, y = map(int, input().split())
        bottles.append((x, y))
    print(get_total_distance(adil_x, adil_y, bera_x, bera_y, recycling_bin_x, recycling_bin_y, bottles))

