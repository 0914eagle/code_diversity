
class LongLongString:
    def __init__(self, string):
        self.string = string

    def __len__(self):
        return len(self.string)

    def __getitem__(self, key):
        return self.string[key]

    def __setitem__(self, key, value):
        self.string = self.string[:key] + value + self.string[key+1:]

def is_identical(program1, program2):
    string1 = LongLongString("")
    string2 = LongLongString("")
    for operation in program1:
        if operation[0] == "D":
            string1 = delete_character(string1, int(operation[1]))
        elif operation[0] == "I":
            string1 = insert_character(string1, int(operation[1]), operation[2])
    for operation in program2:
        if operation[0] == "D":
            string2 = delete_character(string2, int(operation[1]))
        elif operation[0] == "I":
            string2 = insert_character(string2, int(operation[1]), operation[2])
    return string1 == string2

def delete_character(string, position):
    return string[:position] + string[position+1:]

def insert_character(string, position, character):
    return string[:position] + character + string[position:]

if __name__ == '__main__':
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
    print(is_identical(program1, program2))

