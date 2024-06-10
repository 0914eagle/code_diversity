
def get_last_visited_cafe(cafe_indices):
    # find the index of the last visited cafe
    last_visited_cafe = cafe_indices[-1]
    # iterate through the cafe indices in reverse order
    for i in range(len(cafe_indices) - 2, -1, -1):
        # if the current cafe was visited after the last visited cafe, return the last visited cafe
        if cafe_indices[i] > last_visited_cafe:
            return last_visited_cafe
        # otherwise, update the last visited cafe and continue the loop
        last_visited_cafe = cafe_indices[i]
    # if all cafes were visited before the last visited cafe, return the last visited cafe
    return last_visited_cafe

def get_most_forgotten_cafe(cafe_indices):
    # find the index of the most forgotten cafe
    most_forgotten_cafe = None
    # iterate through the cafe indices
    for i in range(len(cafe_indices)):
        # if the current cafe was visited before the most forgotten cafe, update the most forgotten cafe
        if most_forgotten_cafe is None or cafe_indices[i] < most_forgotten_cafe:
            most_forgotten_cafe = cafe_indices[i]
    # return the most forgotten cafe
    return most_forgotten_cafe

if __name__ == '__main__':
    n = int(input())
    cafe_indices = list(map(int, input().split()))
    print(get_most_forgotten_cafe(cafe_indices))

