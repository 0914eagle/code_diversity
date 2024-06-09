
def get_number_of_lights_on(n, m, floors):
    number_of_lights_on = 0
    for floor in floors:
        for i in range(m):
            if floor[2*i] == "1" or floor[2*i+1] == "1":
                number_of_lights_on += 1
    return number_of_lights_on

