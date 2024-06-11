def histogram(test):
    
    # your code here
    # your code here
    if test == '':
        return {}
    else:
        test = test.split()
        test = Counter(test)
        return test

print(histogram('a b c'))
print(histogram('a b b a'))
print(histogram('a b c a b'))
print(histogram('b b b b a'))
print(histogram(''))
/0x01-python-if_else_loops_functions/100-print_tebahpla.py
#!/