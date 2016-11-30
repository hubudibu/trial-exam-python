# Create a function that takes a list as a parameter,
# and returns a new list with all its element's values doubled.
# It should raise an error if the parameter is not a list.

def double_list(values):
    doubled = []
    if type(values) == list:
        for i in values:
            doubled.append(i*2)
        return doubled
    else:
        raise ValueError("Given argument is not a list")

print(double_list(['alma', 'korte', 3]))
