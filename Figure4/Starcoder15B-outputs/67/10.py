def fruit_distribution(s,n):
    
    s = s.split()
    a = int(s[0])
    o = int(s[4])
    return n - a - o

print(fruit_distribution("5 apples and 6 oranges", 19))
print(fruit_distribution("0 apples and 1 oranges",3))
print(fruit_distribution("2 apples and 3 oranges", 100))
print(fruit_distribution("100 apples and 1 oranges",120))

# +
#Task 2
#Write a function that takes a string as an argument and returns a string that is the reverse of the input string.
#For example:
#reverse_string("hello") -> "olleh"
#reverse_string("world") -> "dlrow"

