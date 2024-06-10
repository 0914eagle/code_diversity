
def get_min_max_x(n, d, b, a):
    # Initialize variables
    x_1 = 0
    x_2 = 0
    curr_room = 1
    hidden_students = 0
    
    # Iterate through each room
    for i in range(n):
        # Get the number of students in the current room
        num_students = a[i]
        
        # If the number of students is not equal to the official number, increment the corresponding x variable
        if num_students != b:
            if curr_room == 1:
                x_1 += 1
            else:
                x_2 += 1
        
        # If the current room is not the last room, iterate through the next d rooms
        if i != n - 1:
            for j in range(i + 1, min(n, i + d + 1)):
                # Get the number of students in the next room
                num_students_next = a[j]
                
                # If the number of students in the next room is not equal to the official number, increment the corresponding x variable
                if num_students_next != b:
                    if curr_room == 1:
                        x_1 += 1
                    else:
                        x_2 += 1
        
        # Update the current room and hidden students
        curr_room = (curr_room + 1) % 2
        hidden_students += num_students
    
    # Return the minimum of the two x variables
    return min(x_1, x_2)

def main():
    n, d, b = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_min_max_x(n, d, b, a))

if __name__ == '__main__':
    main()

