
def pyramid_height(n):
    height = 0
    while n > 0:
        height += 1
        n -= height
    return height

