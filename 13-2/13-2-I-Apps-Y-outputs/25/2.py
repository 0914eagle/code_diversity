
def is_connected(stations):
    # Check if there are two stations with different companies
    # and are next to each other
    for i in range(len(stations) - 1):
        if stations[i] != stations[i + 1] and stations[i] != stations[i - 1]:
            return True
    return False

def main():
    stations = input()
    print("Yes") if is_connected(stations) else print("No")

if __name__ == '__main__':
    main()

