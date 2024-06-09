
def get_disintegrated_y_coordinate(droplet, sensors):
    for sensor in sensors:
        if sensor[0] <= droplet[0] <= sensor[1] and sensor[2] <= droplet[1] <= sensor[2]:
            return sensor[2]
    return 0

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
    for droplet in droplets:
        print(get_disintegrated_y_coordinate(droplet, sensors))

if __name__ == '__main__':
    main()

