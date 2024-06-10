
import math

def get_area_covered_by_pickles(pickle_radius, pickles_placed, sandwich_radius):
    
    total_area = 0
    for i in range(pickles_placed):
        x = sandwich_radius * math.cos(2 * math.pi * i / pickles_placed)
        y = sandwich_radius * math.sin(2 * math.pi * i / pickles_placed)
        total_area += math.pi * pickle_radius ** 2 + (x ** 2 + y ** 2 - 2 * pickle_radius ** 2)
    return total_area

def get_max_pickles_placed(sandwich_radius, pickle_radius, max_area_percent):
    
    low = 0
    high = 7
    while low < high:
        mid = (low + high) // 2
        if get_area_covered_by_pickles(pickle_radius, mid, sandwich_radius) <= max_area_percent * math.pi * sandwich_radius ** 2 / 100:
            low = mid + 1
        else:
            high = mid
    return low - 1

def main():
    sandwich_radius, pickle_radius, max_area_percent = map(float, input().split())
    print(get_max_pickles_placed(sandwich_radius, pickle_radius, max_area_percent))

if __name__ == '__main__':
    main()

