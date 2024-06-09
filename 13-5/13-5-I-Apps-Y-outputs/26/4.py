
def f1(n, packages):
    # find the package with the minimum x-coordinate
    min_x = min(packages, key=lambda x: x[0])[0]
    # find the package with the minimum y-coordinate
    min_y = min(packages, key=lambda x: x[1])[1]
    # calculate the distance between the robot and the package with the minimum x-coordinate
    dist_x = abs(min_x)
    # calculate the distance between the robot and the package with the minimum y-coordinate
    dist_y = abs(min_y)
    # if the distance in the x-direction is less than the distance in the y-direction, move only in the x-direction
    if dist_x < dist_y:
        return "R" * dist_x
    # if the distance in the y-direction is less than the distance in the x-direction, move only in the y-direction
    elif dist_y < dist_x:
        return "U" * dist_y
    # if the distances are equal, move in both directions
    else:
        return "RU" * dist_x

def f2(n, packages):
    # find the package with the maximum x-coordinate
    max_x = max(packages, key=lambda x: x[0])[0]
    # find the package with the maximum y-coordinate
    max_y = max(packages, key=lambda x: x[1])[1]
    # calculate the distance between the robot and the package with the maximum x-coordinate
    dist_x = abs(max_x)
    # calculate the distance between the robot and the package with the maximum y-coordinate
    dist_y = abs(max_y)
    # if the distance in the x-direction is less than the distance in the y-direction, move only in the x-direction
    if dist_x < dist_y:
        return "R" * dist_x
    # if the distance in the y-direction is less than the distance in the x-direction, move only in the y-direction
    elif dist_y < dist_x:
        return "U" * dist_y
    # if the distances are equal, move in both directions
    else:
        return "RU" * dist_x

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        packages = []
        for _ in range(n):
            x, y = map(int, input().split())
            packages.append((x, y))
        path = f1(n, packages) + f2(n, packages)
        print("YES")
        print(path)

if __name__ == '__main__':
    main()

