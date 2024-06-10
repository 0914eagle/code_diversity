
def get_optimal_strategy(n, d, b, a):
    # Initialize the number of rooms with different number of students
    x_1 = 0
    x_2 = 0
    
    # Initialize the number of students in each room
    students = [0] * (n + 1)
    
    # Initialize the current room number
    current_room = 1
    
    # Initialize the number of students who have hidden
    hidden_students = 0
    
    # Loop through each room
    for i in range(n):
        # If the current room is not the first or last room
        if current_room != 1 and current_room != n:
            # If the number of students in the current room is different from the official number of students
            if students[current_room] != b:
                # If the current room is processed by the first instructor
                if current_room <= n // 2:
                    # Increment the number of rooms with different number of students for the first instructor
                    x_1 += 1
                # If the current room is processed by the second instructor
                else:
                    # Increment the number of rooms with different number of students for the second instructor
                    x_2 += 1
        
        # If the current room is not the first room
        if current_room != 1:
            # If the number of students in the previous room is different from the official number of students
            if students[current_room - 1] != b:
                # If the previous room is processed by the first instructor
                if (current_room - 1) <= n // 2:
                    # Increment the number of rooms with different number of students for the first instructor
                    x_1 += 1
                # If the previous room is processed by the second instructor
                else:
                    # Increment the number of rooms with different number of students for the second instructor
                    x_2 += 1
        
        # Update the number of students in the current room
        students[current_room] += a[current_room] - hidden_students
        
        # Update the number of hidden students
        hidden_students = 0
        
        # If the current room is not the last room
        if current_room != n:
            # If the number of students in the next room is different from the official number of students
            if students[current_room + 1] != b:
                # If the next room is processed by the first instructor
                if (current_room + 1) <= n // 2:
                    # Increment the number of rooms with different number of students for the first instructor
                    x_1 += 1
                # If the next room is processed by the second instructor
                else:
                    # Increment the number of rooms with different number of students for the second instructor
                    x_2 += 1
        
        # Update the current room number
        current_room += 1
    
    # Return the minimal possible value of the maximum of x_i
    return min(x_1, x_2)

def main():
    # Read the input
    n, d, b = map(int, input().split())
    a = list(map(int, input().split()))
    
    # Call the get_optimal_strategy function and print the result
    print(get_optimal_strategy(n, d, b, a))

if __name__ == '__main__':
    main()

