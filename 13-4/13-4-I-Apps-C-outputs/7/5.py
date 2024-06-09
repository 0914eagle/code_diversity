
def get_covered_length(buildings, D):
    covered_length = 0
    for building in buildings:
        if building[0] == 1:  # there is a transmitter on top of the building
            covered_length += building[2]  # add the height of the building to the covered length
        else:  # there is no transmitter on top of the building
            covered_length = max(covered_length, building[2])  # update the covered length with the maximum of the current covered length and the height of the building
    return covered_length

