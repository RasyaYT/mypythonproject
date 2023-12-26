def sum_floats(*args):
    return sum(arg for arg in args if type(arg) == float)

print(sum_floats(type(2222)))