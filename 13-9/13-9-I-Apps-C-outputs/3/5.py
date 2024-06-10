
def get_program(input_string):
    program = []
    for line in input_string.splitlines():
        if line.startswith("D"):
            program.append(("D", int(line[2:])))
        elif line.startswith("I"):
            program.append(("I", int(line[2:line.find(" ")]), line[line.find(" ")+1]))
        else:
            program.append(("E",))
    return program

def compare_programs(program1, program2):
    if len(program1) != len(program2):
        return False
    for i in range(len(program1)):
        if program1[i] != program2[i]:
            return False
    return True

def main():
    program1 = get_program(input())
    program2 = get_program(input())
    print(int(compare_programs(program1, program2)))

if __name__ == '__main__':
    main()

