
def get_farthest_cow(k, cows):
    # Find the index of the first unoccupied room for Farmer John
    farmer_john_index = cows.index(0)
    
    # Find the index of the first unoccupied room for the farthest cow
    farthest_cow_index = cows.index(0, farmer_john_index + 1)
    
    # Return the distance between Farmer John's room and the farthest cow's room
    return abs(farmer_john_index - farthest_cow_index)

def main():
    n, k = map(int, input().split())
    cows = list(input())
    
    print(get_farthest_cow(k, cows))

if __name__ == '__main__':
    main()

