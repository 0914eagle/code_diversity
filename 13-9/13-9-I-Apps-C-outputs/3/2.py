
class LongLongString:
    def __init__(self, string):
        self.string = string

    def __len__(self):
        return len(self.string)

    def __getitem__(self, key):
        return self.string[key]

    def __setitem__(self, key, value):
        self.string = self.string[:key] + value + self.string[key+1:]

    def __delitem__(self, key):
        self.string = self.string[:key] + self.string[key+1:]

def read_program(file_name):
    with open(file_name, "r") as f:
        program = []
        for line in f:
            if line.startswith("D "):
                program.append(("D", int(line[2:])))
            elif line.startswith("I "):
                program.append(("I", int(line[2:line.find(" ")]), line[line.find(" ")+1]))
            elif line.startswith("E"):
                break
        return program

def compare_programs(program1, program2):
    string1 = LongLongString("")
    string2 = LongLongString("")
    for op in program1:
        if op[0] == "D":
            string1.__delitem__(op[1])
        elif op[0] == "I":
            string1.__setitem__(op[1], op[2])
    for op in program2:
        if op[0] == "D":
            string2.__delitem__(op[1])
        elif op[0] == "I":
            string2.__setitem__(op[1], op[2])
    return string1 == string2

def main():
    program1 = read_program("program1.txt")
    program2 = read_program("program2.txt")
    if compare_programs(program1, program2):
        print("0")
    else:
        print("1")

if __name__ == '__main__':
    main()

