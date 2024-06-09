
def get_number_of_pyramids(n):
    number_of_pyramids = 0
    while n > 0:
        if n == 1:
            number_of_pyramids += 1
            break
        else:
            height = 1
            while n - height * (height + 1) // 2 >= 0:
                height += 1
            number_of_pyramids += 1
            n -= height * (height + 1) // 2
    return number_of_pyramids

