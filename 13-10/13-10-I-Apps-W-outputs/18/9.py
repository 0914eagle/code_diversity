
def find_unvisited_cafe(cafe_indices):
    # find the last visited cafe
    last_visited_cafe = cafe_indices[-1]
    # find the indices of cafes that were visited before the last visited cafe
    visited_before_last_visited_cafe = [i for i in cafe_indices if i < last_visited_cafe]
    # find the maximum index of cafes that were visited before the last visited cafe
    max_visited_before_last_visited_cafe = max(visited_before_last_visited_cafe) if visited_before_last_visited_cafe else -1
    # return the unvisited cafe with the maximum index
    return max_visited_before_last_visited_cafe + 1

def main():
    n = int(input())
    cafe_indices = [int(i) for i in input().split()]
    print(find_unvisited_cafe(cafe_indices))

if __name__ == '__main__':
    main()

