
def is_tourist_friendly(road_network):
    # Check if the road network is tourist-friendly
    # Return True if it is, False otherwise
    pass

def redirect_roads(road_network):
    # Redirect some of the roads to make the road network tourist-friendly
    # Return the redirected road network
    pass

def main():
    # Read the input
    n, e = map(int, input().split())
    road_network = []
    for _ in range(e):
        a, b = map(int, input().split())
        road_network.append((a, b))
    
    # Check if the road network is tourist-friendly
    if is_tourist_friendly(road_network):
        print("YES")
        # If it is, print the redirected road network
        for road in redirect_roads(road_network):
            print(*road)
    else:
        print("NO")

if __name__ == "__main__":
    main()

