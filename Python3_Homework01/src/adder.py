"""
Take two objects and add them if both are int
"""

def adder_errors(val1, val2):
    
    if (isinstance(val1, int)
    and isinstance(val2, int)):
        result = val1 + val2
    else:
        raise TypeError("String values can not be added")
    return
