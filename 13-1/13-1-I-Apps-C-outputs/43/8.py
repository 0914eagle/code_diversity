
def is_equivalent(str1, str2):
    if str1 == str2:
        return "YES"
    
    n = len(str1) // 2
    str1_1, str1_2 = str1[:n], str1[n:]
    str2_1, str2_2 = str2[:n], str2[n:]
    
    if str1_1 == str2_2 and str1_2 == str2_1:
        return "YES"
    else:
        return "NO"
    
if __name__ == '__main__':
    str1 = input()
    str2 = input()
    print(is_equivalent(str1, str2))

