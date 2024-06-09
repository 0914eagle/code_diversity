
def find_disintegrated_droplets(droplets, sensors):
    disintegrated_droplets = []
    for droplet in droplets:
        for sensor in sensors:
            if droplet[0] >= sensor[0] and droplet[0] <= sensor[1] and droplet[1] == sensor[2]:
                disintegrated_droplets.append(droplet[1])
                break
        else:
            disintegrated_droplets.append(0)
    return disintegrated_droplets

def main():
    num_droplets, num_sensors = map(int, input().split())
    droplets = []
    for _ in range(num_droplets):
        x, y = map(int, input().split())
        droplets.append((x, y))
    sensors = []
    for _ in range(num_sensors):
        x1, x2, y = map(int, input().split())
        sensors.append((x1, x2, y))
    disintegrated_droplets = find_disintegrated_droplets(droplets, sensors)
    for y in disintegrated_droplets:
        print(y)

if __name__ == '__main__':
    main()

