
def get_last_visited_cafe(cafe_indices):
    # find the index of the last visited cafe
    last_visited_cafe = cafe_indices[-1]
    
    # find the indices of all cafes that were visited after the last visit to the last visited cafe
    cafes_visited_after_last = [cafe for cafe in cafe_indices if cafe > last_visited_cafe]
    
    # if there are no cafes that were visited after the last visit to the last visited cafe, then the last visited cafe is the answer
    if not cafes_visited_after_last:
        return last_visited_cafe
    
    # otherwise, find the index of the cafe that was visited before the last visit to the last visited cafe
    cafes_visited_before_last = [cafe for cafe in cafe_indices if cafe < last_visited_cafe]
    if not cafes_visited_before_last:
        return last_visited_cafe
    else:
        return min(cafes_visited_before_last)

def main():
    n = int(input())
    cafe_indices = [int(cafe) for cafe in input().split()]
    print(get_last_visited_cafe(cafe_indices))

if __name__ == '__main__':
    main()

