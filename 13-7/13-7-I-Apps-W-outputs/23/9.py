
def get_min_time(n, s, people):
    # Initialize the minimum time needed to reach both points as infinity
    min_time = float('inf')
    
    # Iterate over all possible positions of the bomb
    for bomb_pos in range(0, 10**6):
        # Initialize the time needed to reach both points as infinity
        time_0 = float('inf')
        time_1000000 = float('inf')
        
        # Iterate over all people
        for person in people:
            # Calculate the time needed to reach the bomb from the current person's position
            time_bomb = abs(bomb_pos - person[0]) / person[1]
            
            # Calculate the time needed to reach point 0 from the bomb
            time_0_from_bomb = (10**6 - bomb_pos) / s
            
            # Calculate the time needed to reach point 1000000 from the bomb
            time_1000000_from_bomb = (bomb_pos) / s
            
            # Calculate the minimum time needed to reach both points from the current person's position
            time_0 = min(time_0, time_bomb + time_0_from_bomb)
            time_1000000 = min(time_1000000, time_bomb + time_1000000_from_bomb)
        
        # Calculate the minimum time needed to reach both points from the current bomb position
        min_time = min(min_time, time_0 + time_1000000)
    
    return min_time

def main():
    n, s = map(int, input().split())
    people = []
    for _ in range(n):
        x, v, t = map(int, input().split())
        people.append((x, v, t))
    print(get_min_time(n, s, people))

if __name__ == '__main__':
    main()

