
def f1(droplets, sensors):
    # Function to check if a droplet will disintegrate
    def will_disintegrate(droplet, sensor):
        return droplet[1] <= sensor[1] and droplet[2] >= sensor[2]

    # Function to find the y-coordinate of the disintegration
    def find_disintegration(droplet, sensors):
        for sensor in sensors:
            if will_disintegrate(droplet, sensor):
                return sensor[2]
        return 0

    # Find the disintegration point for each droplet
    disintegrations = [find_disintegration(droplet, sensors) for droplet in droplets]

    return disintegrations

def f2(droplets, sensors):
    # Function to check if a droplet will disintegrate
    def will_disintegrate(droplet, sensor):
        return droplet[1] <= sensor[1] and droplet[2] >= sensor[2]

    # Function to find the y-coordinate of the disintegration
    def find_disintegration(droplet, sensors):
        for sensor in sensors:
            if will_disintegrate(droplet, sensor):
                return sensor[2]
        return 0

    # Find the disintegration point for each droplet
    disintegrations = [find_disintegration(droplet, sensors) for droplet in droplets]

    return disintegrations

if __name__ == '__main__':
    droplets = [(1, 8), (2, 3), (2, 8), (5, 8), (5, 9)]
    sensors = [(3, 6, 6), (1, 7, 4), (1, 3, 1)]
    print(f1(droplets, sensors))
    print(f2(droplets, sensors))

