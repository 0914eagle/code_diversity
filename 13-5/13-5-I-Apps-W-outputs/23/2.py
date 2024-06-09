
def get_shelter_capacity(shelter_capacities):
    return sum(shelter_capacities)

def get_total_people(people_per_location):
    return sum(people_per_location)

def get_shelters_needed(total_people, shelter_capacity):
    return total_people // shelter_capacity + (total_people % shelter_capacity > 0)

def get_min_time_to_shelter(people_per_location, shelters, roads):
    total_people = get_total_people(people_per_location)
    shelter_capacity = get_shelter_capacity(shelters)
    shelters_needed = get_shelters_needed(total_people, shelter_capacity)
    if shelters_needed > len(shelters):
        return -1
    time = 0
    for person in range(total_people):
        current_location = 1
        while True:
            next_location = people_per_location[current_location - 1]
            if next_location == 0:
                break
            current_location = next_location
            time += roads[(current_location, next_location)]
        time += shelters[current_location - 1][1]
    return time

def main():
    n, m, s = map(int, input().split())
    people_per_location = list(map(int, input().split()))
    roads = {}
    for _ in range(m):
        u, v, w = map(int, input().split())
        roads[(u, v)] = w
        roads[(v, u)] = w
    shelters = []
    for _ in range(s):
        s, c = map(int, input().split())
        shelters.append((s, c))
    print(get_min_time_to_shelter(people_per_location, shelters, roads))

if __name__ == '__main__':
    main()

