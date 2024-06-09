
def f1(n, k, commands):
    # Initialize the egg holder and the number of children
    egg_holder = 0
    num_children = n
    
    # Iterate through the commands
    for command in commands:
        # If the command is a number, throw the egg that number of positions clockwise
        if command.isdigit():
            egg_holder = (egg_holder + int(command)) % num_children
        # If the command is undo, undo the last m throws
        else:
            m = int(command.split()[1])
            egg_holder = (egg_holder - m) % num_children
            if egg_holder < 0:
                egg_holder += num_children
    
    # Return the number of the child with the egg
    return egg_holder

def f2(...):
    # Implement function f2 here
    pass

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    commands = input().split()
    print(f1(n, k, commands))

