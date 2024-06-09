
def find_disintegration_points(droplets, sensors):
    disintegration_points = []
    for droplet in droplets:
        for sensor in sensors:
            if sensor[0] <= droplet[0] <= sensor[1] and sensor[2] == droplet[1]:
                disintegration_points.append(sensor[2])
                break
        else:
            disintegration_points.append(0)
    return disintegration_points

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
    disintegration_points = find_disintegration_points(droplets, sensors)
    for point in disintegration_points:
        print(point)

if __name__ == '__main__':
    main()

