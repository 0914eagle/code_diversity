
def solve(droplets, sensors):
    result = []
    for droplet in droplets:
        for sensor in sensors:
            if sensor[0] <= droplet[0] <= sensor[1] and droplet[1] == sensor[2]:
                result.append(sensor[2])
                break
        else:
            result.append(0)
    return result

