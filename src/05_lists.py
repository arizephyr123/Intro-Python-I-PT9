# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
x.append(4)
a=x
print(a)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
x.extend(y)
b=x
print(b)

# Change x so that it is [1, 2, 3, 4, 9, 10]
x.remove(8)
c=x
print(c)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
x.insert(-1, 99)
d=x
print(d)

# Print the length of list x
print(len(x))

# Print all the values in x multiplied by 1000
for num in x:
    print(num * 1000)