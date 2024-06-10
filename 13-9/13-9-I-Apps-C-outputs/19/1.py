
def read_input():
    N = int(input())
    lamps = []
    for i in range(N):
        x, y, e = map(int, input().split())
        lamps.append((x, y, e))
    return N, lamps

def get_line_length(N, lamps):
    # Find the shortest continuous line that divides the positive and negative energy sources in the room
    # The line should pass through the centers of the lamps
    x_coords = [lamp[0] for lamp in lamps]
    y_coords = [lamp[1] for lamp in lamps]
    x_pos = [lamp[0] for lamp in lamps if lamp[2] > 0]
    x_neg = [lamp[0] for lamp in lamps if lamp[2] < 0]
    y_pos = [lamp[1] for lamp in lamps if lamp[2] > 0]
    y_neg = [lamp[1] for lamp in lamps if lamp[2] < 0]

    x_pos_min = min(x_pos)
    x_pos_max = max(x_pos)
    x_neg_min = min(x_neg)
    x_neg_max = max(x_neg)
    y_pos_min = min(y_pos)
    y_pos_max = max(y_pos)
    y_neg_min = min(y_neg)
    y_neg_max = max(y_neg)

    pos_x_coords = [coord for coord in x_coords if coord >= x_pos_min and coord <= x_pos_max]
    neg_x_coords = [coord for coord in x_coords if coord >= x_neg_min and coord <= x_neg_max]
    pos_y_coords = [coord for coord in y_coords if coord >= y_pos_min and coord <= y_pos_max]
    neg_y_coords = [coord for coord in y_coords if coord >= y_neg_min and coord <= y_neg_max]

    line_length = float('inf')
    for x_coord in pos_x_coords:
        for y_coord in pos_y_coords:
            pos_energy = sum(lamp[2] for lamp in lamps if lamp[0] == x_coord and lamp[1] == y_coord and lamp[2] > 0)
            neg_energy = sum(lamp[2] for lamp in lamps if lamp[0] == x_coord and lamp[1] == y_coord and lamp[2] < 0)
            if pos_energy == neg_energy:
                line_length = min(line_length, abs(x_coord - x_neg_min) + abs(y_coord - y_neg_min))
    for x_coord in neg_x_coords:
        for y_coord in neg_y_coords:
            pos_energy = sum(lamp[2] for lamp in lamps if lamp[0] == x_coord and lamp[1] == y_coord and lamp[2] > 0)
            neg_energy = sum(lamp[2] for lamp in lamps if lamp[0] == x_coord and lamp[1] == y_coord and lamp[2] < 0)
            if pos_energy == neg_energy:
                line_length = min(line_length, abs(x_coord - x_pos_min) + abs(y_coord - y_pos_min))

    if line_length == float('inf'):
        return 'IMPOSSIBLE'
    else:
        return line_length

def main():
    N, lamps = read_input()
    print(get_line_length(N, lamps))

if __name__ == '__main__':
    main()

