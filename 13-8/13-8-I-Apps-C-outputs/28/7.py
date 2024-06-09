
def is_valid_string(string, edges):
    n = len(string)
    for i in range(n):
        for j in range(i+1, n):
            if string[i] == string[j]:
                return False
            if abs(ord(string[i]) - ord(string[j])) != 1:
                return False
    for edge in edges:
        if string[edge[0]-1] == string[edge[1]-1]:
            return False
    return True

