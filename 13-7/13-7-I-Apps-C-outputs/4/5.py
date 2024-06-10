
def get_max_gems(n, r, w, h, gems):
    # Initialize variables
    max_gems = 0
    current_gems = 0
    current_x = 0
    current_y = 0
    horizontal_velocity = 0
    vertical_velocity = 0
    velocity = 0
    time = 0

    # Sort the gems by their x coordinate in ascending order
    gems.sort(key=lambda x: x[0])

    # Loop through each gem and calculate the time it takes to reach it
    for gem in gems:
        gem_x = gem[0]
        gem_y = gem[1]
        time_to_reach_gem = (gem_x - current_x) / horizontal_velocity
        time += time_to_reach_gem
        current_x = gem_x
        current_y = gem_y
        current_gems += 1
        max_gems = max(max_gems, current_gems)

    # Return the maximum number of gems collected
    return max_gems

def main():
    n, r, w, h = map(int, input().split())
    gems = []
    for _ in range(n):
        x, y = map(int, input().split())
        gems.append((x, y))
    print(get_max_gems(n, r, w, h, gems))

if __name__ == '__main__':
    main()

