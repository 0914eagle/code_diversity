
def solve(s):
    n = len(s)
    count = [s.count(i) for i in "012"]
    if count == [n//3, n//3, n//3]:
        return s
    
    # find the smallest element in the count list
    smallest = min(count)
    # find the index of the smallest element in the count list
    smallest_index = count.index(smallest)
    
    # create a new string with the smallest element replaced by '0'
    new_s = s[:smallest_index] + "0" + s[smallest_index+1:]
    return new_s

