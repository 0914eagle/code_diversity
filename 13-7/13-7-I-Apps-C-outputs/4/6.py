
def get_max_gems(n, r, w, h, gems):
    # Initialize variables
    max_gems = 0
    current_gems = 0
    current_x = 0
    current_y = 0
    vertical_speed = 1
    horizontal_speed = 1

    # Sort the gems by their y-coordinate in descending order
    gems.sort(key=lambda x: x[1], reverse=True)

    # Iterate through the gems and check if they can be collected
    for gem in gems:
        x, y = gem
        distance = abs(current_x - x)
        time = distance / horizontal_speed
        if current_y - time * vertical_speed >= y:
            current_gems += 1
            current_x = x
            current_y = y
        if current_gems > max_gems:
            max_gems = current_gems

    return max_gems

def main():
    n, r, w, h = map(int, input().split())
    gems = []
    for i in range(n):
        x, y = map(int, input().split())
        gems.append((x, y))
    print(get_max_gems(n, r, w, h, gems))

if __name__ == '__main__':
    main()

