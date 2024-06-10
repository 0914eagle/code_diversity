
import math

def calculate_distance(t1, t2):
    # Calculate the distance between t1 and t2
    distance = math.fabs(t1 - t2)
    
    # If the distance is greater than 6, then Misha has to go around the clock face
    if distance > 6:
        distance = 12 - distance
    
    return distance

def can_prepare_contest(h, m, s, t1, t2):
    # Calculate the distance between t1 and t2
    distance = calculate_distance(t1, t2)
    
    # If the distance is less than or equal to the hand's length, then Misha can prepare the contest on time
    if distance <= 1:
        return "YES"
    else:
        return "NO"

def main():
    h, m, s, t1, t2 = map(int, input().split())
    print(can_prepare_contest(h, m, s, t1, t2))

if __name__ == '__main__':
    main()

