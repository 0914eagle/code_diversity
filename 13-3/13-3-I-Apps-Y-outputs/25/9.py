
def simplicity(string):
    return len(set(string))

def min_erase(string):
    simplicity_before = simplicity(string)
    if simplicity_before <= 2:
        return 0
    else:
        for i in range(len(string)):
            string_erased = string[:i] + string[i+1:]
            simplicity_after = simplicity(string_erased)
            if simplicity_after <= 2:
                return len(string) - len(string_erased)
        return len(string)

print(min_erase("string"))
print(min_erase("letter"))
print(min_erase("aaaaaa"))
print(min_erase("uncopyrightable"))
print(min_erase("ambidextrously"))
print(min_erase("assesses"))

