
def get_required_recorders(programs):
    # Sort the programs by their start time
    programs.sort(key=lambda x: x[0])
    
    # Initialize the number of recorders needed
    recorders_needed = 1
    
    # Iterate through the programs
    for i in range(len(programs)):
        # Get the current program
        program = programs[i]
        
        # Check if the program can be recorded by the current recorder
        if program[0] >= recorders_needed:
            # Increment the number of recorders needed
            recorders_needed += 1
    
    return recorders_needed

def main():
    # Read the number of programs and channels from stdin
    n_programs, n_channels = map(int, input().split())
    
    # Read the programs from stdin
    programs = []
    for _ in range(n_programs):
        s, t, c = map(int, input().split())
        programs.append((s, t, c))
    
    # Get the required number of recorders
    recorders_needed = get_required_recorders(programs)
    
    # Print the result
    print(recorders_needed)

if __name__ == '__main__':
    main()

