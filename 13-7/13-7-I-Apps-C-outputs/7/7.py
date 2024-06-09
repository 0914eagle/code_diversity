
def get_total_area(plots):
    total_area = 0
    for plot in plots:
        width = plot[2] - plot[0]
        height = plot[3] - plot[1]
        total_area += width * height
    return round(total_area, 2)

