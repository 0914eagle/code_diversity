
def get_max_fragment_area(w, h, cuts):
    # Initialize the maximum fragment area and its position
    max_area = w * h
    max_area_position = (0, 0, w, h)
    
    # Iterate through the cuts
    for cut in cuts:
        # Get the current fragment area and its position
        current_area = get_fragment_area(w, h, cut)
        current_position = get_fragment_position(w, h, cut)
        
        # Update the maximum fragment area and its position if necessary
        if current_area > max_area:
            max_area = current_area
            max_area_position = current_position
    
    return max_area_position

def get_fragment_area(w, h, cut):
    # Get the coordinates of the cut
    x1, y1, x2, y2 = cut
    
    # Calculate the area of the fragment
    area = (x2 - x1) * (y2 - y1)
    
    return area

def get_fragment_position(w, h, cut):
    # Get the coordinates of the cut
    x1, y1, x2, y2 = cut
    
    # Calculate the position of the fragment
    position = (x1, y1, x2, y2)
    
    return position

def main():
    w, h, n = map(int, input().split())
    cuts = []
    for _ in range(n):
        cut = input()
        if cut[0] == 'H':
            y = int(cut[2:])
            cuts.append((0, y, w, h))
        elif cut[0] == 'V':
            x = int(cut[2:])
            cuts.append((x, 0, w, h))
    
    max_area_position = get_max_fragment_area(w, h, cuts)
    print(max_area_position[2] * max_area_position[3])

if __name__ == '__main__':
    main()

