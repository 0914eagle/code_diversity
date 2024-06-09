
def get_number_of_lit_flats(n, m, floors):
    number_of_lit_flats = 0
    for floor in floors:
        for i in range(m):
            if floor[2*i] == "1" or floor[2*i+1] == "1":
                number_of_lit_flats += 1
    return number_of_lit_flats

