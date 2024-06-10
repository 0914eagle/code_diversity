
def get_max_gems(n, r, w, h, gems):
    # Initialize variables
    max_gems = 0
    current_gems = 0
    current_x = 0
    current_y = 0
    velocity_x = 0
    velocity_y = v

    # Sort the gems by their y-coordinate in descending order
    sorted_gems = sorted(gems, key=lambda x: x[1], reverse=True)

    # Iterate through the gems and calculate the maximum number of gems that can be collected
    for gem in sorted_gems:
        x, y = gem
        distance = abs(current_x - x)
        time = distance / velocity_x
        if time < velocity_y:
            current_gems += 1
        else:
            if current_gems > max_gems:
                max_gems = current_gems
            current_gems = 1
        current_x = x
        current_y = y

    # Return the maximum number of gems that can be collected
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

