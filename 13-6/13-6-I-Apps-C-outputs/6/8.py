
def antimatter_rain(droplets, sensors):
    disintegrated_droplets = []
    for droplet in droplets:
        for sensor in sensors:
            if droplet[0] >= sensor[0] and droplet[0] <= sensor[1] and droplet[1] == sensor[2]:
                disintegrated_droplets.append(droplet[1])
                break
        else:
            disintegrated_droplets.append(0)
    return disintegrated_droplets

