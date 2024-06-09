
class LongLongString:
    def __init__(self, string):
        self.string = string

    def __len__(self):
        return len(self.string)

    def __getitem__(self, index):
        return self.string[index]

    def __setitem__(self, index, char):
        self.string = self.string[:index] + char + self.string[index+1:]

    def __delitem__(self, index):
        self.string = self.string[:index] + self.string[index+1:]

def compare_dna_programs(program1, program2):
    string1 = LongLongString("")
    string2 = LongLongString("")

    for operation in program1:
        if operation[0] == "D":
            string1.__delitem__(int(operation[1]))
        elif operation[0] == "I":
            string1.__setitem__(int(operation[1]), operation[2])

    for operation in program2:
        if operation[0] == "D":
            string2.__delitem__(int(operation[1]))
        elif operation[0] == "I":
            string2.__setitem__(int(operation[1]), operation[2])

    return string1.string == string2.string

def main():
    program1 = []
    program2 = []

    while True:
        line = input()
        if line == "E":
            break
        operation = line.split()
        if operation[0] == "D":
            program1.append(operation)
        elif operation[0] == "I":
            program2.append(operation)

    print(compare_dna_programs(program1, program2))

if __name__ == "__main__":
    main()

