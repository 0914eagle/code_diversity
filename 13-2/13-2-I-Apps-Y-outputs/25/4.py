
def is_bus_service_available(stations):
    # Check if there are two stations with different companies
    if stations[0] != stations[1] and stations[1] != stations[2]:
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    stations = input()
    print(is_bus_service_available(stations))

