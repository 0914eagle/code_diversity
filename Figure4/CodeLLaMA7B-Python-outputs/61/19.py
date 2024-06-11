def correct_bracketing(brackets: str):
    
    # Your code here
    # 1. 找到第一个左括号，记录下位置
    # 2. 从第一个左括号开始，找到第一个右括号，记录下位置
    # 3. 如果位置相等，则表示找到了一个完整的括号对，继续找下一个左括号
    # 4. 如果位置不相等，则表示找到了一个不完整的括号对，返回False
    # 5. 如果找完了，仍然有左括号没有右括号，则返回False
    # 6. 如果找完了，没有左括号没有右括号，则返回True
    if len(brackets) == 0:
        return True
    if brackets[0] == '(':
        return False
    if brackets[0] == ')':
        return False
    if brackets[0] == '(':
        return correct_bracketing(brackets[1:])
    if brackets[0] == ')':
        return correct_bracketing(brackets[1:])


if __name__ == '__main__':
    import doctest
    doctest.testmod()