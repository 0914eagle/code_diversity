
def get_total_area(plots):
    total_area = 0
    for plot in plots:
        area = (plot[2] - plot[0]) * (plot[3] - plot[1])
        total_area += area
    return round(total_area, 2)

