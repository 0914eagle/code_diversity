
def get_recorders_needed(n, c, programs):
    # Sort the programs by their start time
    programs.sort(key=lambda x: x[0])
    
    # Initialize the number of recorders needed to 0
    recorders_needed = 0
    
    # Iterate through the programs
    for program in programs:
        # Check if the current program can be recorded with the current number of recorders
        if recorders_needed < program[2]:
            # If not, add a new recorder
            recorders_needed += 1
    
    return recorders_needed

def main():
    n, c = map(int, input().split())
    programs = []
    for _ in range(n):
        s, t, c = map(int, input().split())
        programs.append([s, t, c])
    
    print(get_recorders_needed(n, c, programs))

if __name__ == '__main__':
    main()

