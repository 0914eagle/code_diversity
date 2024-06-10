
def get_cafe_index(cafe_indices, n):
    # find the index of the last cafe visited
    last_cafe_index = cafe_indices[-1]
    
    # find the indices of all cafes visited after the last cafe
    after_last_cafe_indices = [i for i in cafe_indices if i > last_cafe_index]
    
    # find the index of the cafe visited before the last cafe
    before_last_cafe_index = cafe_indices[-2]
    
    # check if the before_last_cafe_index is not in the after_last_cafe_indices list
    if before_last_cafe_index not in after_last_cafe_indices:
        return before_last_cafe_index
    
    # if the before_last_cafe_index is in the after_last_cafe_indices list,
    # find the index of the cafe visited before the before_last_cafe_index
    before_before_last_cafe_index = cafe_indices[-3]
    
    # check if the before_before_last_cafe_index is not in the after_last_cafe_indices list
    if before_before_last_cafe_index not in after_last_cafe_indices:
        return before_before_last_cafe_index
    
    # if the before_before_last_cafe_index is also in the after_last_cafe_indices list,
    # repeat the process until the cafe visited before the before_before_last_cafe_index is not in the after_last_cafe_indices list
    while before_before_last_cafe_index in after_last_cafe_indices:
        before_before_last_cafe_index = cafe_indices[-(n-1)]
        n -= 1
    
    return before_before_last_cafe_index

def main():
    n = int(input())
    cafe_indices = list(map(int, input().split()))
    print(get_cafe_index(cafe_indices, n))

if __name__ == '__main__':
    main()

