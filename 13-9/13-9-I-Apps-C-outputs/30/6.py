
def clock_paradox(h, m, s, t_1, t_2):
    # Convert the input times to integers
    h = int(h)
    m = int(m)
    s = int(s)
    t_1 = int(t_1)
    t_2 = int(t_2)
    
    # Check if the target time is the same as the starting time
    if t_1 == t_2:
        return "NO"
    
    # Check if the target time is within the range of the hands
    if t_2 < 1 or t_2 > 12:
        return "NO"
    
    # Check if the starting time is within the range of the hands
    if t_1 < 1 or t_1 > 12:
        return "NO"
    
    # Check if the target time is on the same arc as the starting time
    if t_1 <= 6 and t_2 <= 6:
        return "YES"
    if t_1 > 6 and t_2 > 6:
        return "YES"
    
    # Check if the target time is on the opposite arc as the starting time
    if t_1 <= 6 and t_2 > 6:
        return "NO"
    if t_1 > 6 and t_2 <= 6:
        return "NO"
    
    # Check if the target time is on the same side of the 12-hour mark as the starting time
    if t_1 <= 6 and t_2 > 6:
        return "YES"
    if t_1 > 6 and t_2 <= 6:
        return "YES"
    
    # Check if the target time is on the opposite side of the 12-hour mark as the starting time
    if t_1 <= 6 and t_2 < 12:
        return "NO"
    if t_1 > 6 and t_2 > 12:
        return "NO"
    
    # If none of the above conditions are met, return "NO"
    return "NO"

def main():
    h = input("Enter the hour: ")
    m = input("Enter the minute: ")
    s = input("Enter the second: ")
    t_1 = input("Enter the starting time: ")
    t_2 = input("Enter the target time: ")
    
    print(clock_paradox(h, m, s, t_1, t_2))

if __name__ == '__main__':
    main()

