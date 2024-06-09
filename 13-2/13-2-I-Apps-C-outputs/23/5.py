
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

    def __str__(self):
        return self.string

def compare_dna_programs(program1, program2):
    string1 = LongLongString("")
    string2 = LongLongString("")

    for operation in program1:
        if operation[0] == "D":
            string1.__delitem__(int(operation[1:]))
        elif operation[0] == "I":
            string1.__setitem__(int(operation[1:]), operation[3])

    for operation in program2:
        if operation[0] == "D":
            string2.__delitem__(int(operation[1:]))
        elif operation[0] == "I":
            string2.__setitem__(int(operation[1:]), operation[3])

    return string1 == string2

def main():
    program1 = []
    program2 = []

    while True:
        line = input()
        if line == "E":
            break
        else:
            program1.append(line)

    while True:
        line = input()
        if line == "E":
            break
        else:
            program2.append(line)

    print(compare_dna_programs(program1, program2))

if __name__ == "__main__":
    main()

