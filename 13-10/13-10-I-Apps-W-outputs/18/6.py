
def get_last_visit_time(cafe_id, visited_cafes):
    return visited_cafes[cafe_id]

def get_non_repeating_cafe(cafe_ids, visited_cafes):
    last_visit_times = [get_last_visit_time(cafe_id, visited_cafes) for cafe_id in cafe_ids]
    return cafe_ids[last_visit_times.index(max(last_visit_times))]

def main():
    n = int(input())
    visited_cafes = {}
    for i in range(n):
        cafe_id = int(input())
        if cafe_id not in visited_cafes:
            visited_cafes[cafe_id] = 0
        visited_cafes[cafe_id] += 1
    cafe_ids = list(visited_cafes.keys())
    print(get_non_repeating_cafe(cafe_ids, visited_cafes))

if __name__ == '__main__':
    main()

