
def get_positive_energy_lamp_coordinates(lamp_list):
    positive_energy_lamp_coordinates = []
    for lamp in lamp_list:
        if lamp[2] > 0:
            positive_energy_lamp_coordinates.append(lamp[:2])
    return positive_energy_lamp_coordinates

def get_negative_energy_lamp_coordinates(lamp_list):
    negative_energy_lamp_coordinates = []
    for lamp in lamp_list:
        if lamp[2] < 0:
            negative_energy_lamp_coordinates.append(lamp[:2])
    return negative_energy_lamp_coordinates

def get_line_length(positive_energy_lamp_coordinates, negative_energy_lamp_coordinates):
    min_length = float('inf')
    for positive_energy_lamp in positive_energy_lamp_coordinates:
        for negative_energy_lamp in negative_energy_lamp_coordinates:
            length = abs(positive_energy_lamp[0] - negative_energy_lamp[0]) + abs(positive_energy_lamp[1] - negative_energy_lamp[1])
            if length < min_length:
                min_length = length
    return min_length

def main():
    lamp_list = []
    num_lamp = int(input())
    for i in range(num_lamp):
        lamp_list.append(list(map(int, input().split())))
    positive_energy_lamp_coordinates = get_positive_energy_lamp_coordinates(lamp_list)
    negative_energy_lamp_coordinates = get_negative_energy_lamp_coordinates(lamp_list)
    line_length = get_line_length(positive_energy_lamp_coordinates, negative_energy_lamp_coordinates)
    print(line_length)

if __name__ == '__main__':
    main()

