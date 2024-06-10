
import sys

class LongLongString:
    def __init__(self, string):
        self.string = string

    def __len__(self):
        return len(self.string)

    def __getitem__(self, key):
        return self.string[key]

    def __setitem__(self, key, value):
        self.string = self.string[:key] + value + self.string[key+1:]

    def __str__(self):
        return self.string

    def __repr__(self):
        return self.string

def read_program(input_file):
    program = []
    for line in input_file:
        operation, arg = line.strip().split()
        if operation == "D":
            program.append(("D", int(arg)))
        elif operation == "I":
            program.append(("I", int(arg), line[len(operation)+len(arg)+1]))
        else:
            break
    return program

def apply_program(program, string):
    for op in program:
        if op[0] == "D":
            string = string[:op[1]] + string[op[1]+1:]
        elif op[0] == "I":
            string = string[:op[1]] + op[2] + string[op[1]:]
    return string

def compare_programs(program1, program2):
    string = LongLongString("X")
    string1 = apply_program(program1, string)
    string2 = apply_program(program2, string)
    return string1 == string2

if __name__ == '__main__':
    input_file = open(sys.argv[1], 'r')
    program1 = read_program(input_file)
    program2 = read_program(input_file)
    print(compare_programs(program1, program2))

