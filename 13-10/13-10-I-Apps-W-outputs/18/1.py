
def get_last_visited_cafe(visited_cafes):
    # find the index of the last visited cafe
    last_visited_cafe = visited_cafes[-1]
    # find the indices of all cafes that were visited after the last visited cafe
    after_last_visited_cafes = [i for i in visited_cafes if i > last_visited_cafe]
    # if there are no cafes that were visited after the last visited cafe, return the last visited cafe
    if not after_last_visited_cafes:
        return last_visited_cafe
    # otherwise, return the index of the last cafe that was visited before the last visited cafe
    return after_last_visited_cafes[-1] - 1

def main():
    n = int(input())
    visited_cafes = [int(x) for x in input().split()]
    print(get_last_visited_cafe(visited_cafes))

if __name__ == '__main__':
    main()

