
def count_sausages_on_crust(r, d, n, sausages):
    count = 0
    for sausage in sausages:
        x, y, r = sausage
        if x**2 + y**2 + r**2 <= (r-d)**2:
            count += 1
    return count

