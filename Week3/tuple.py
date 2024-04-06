"""
Tuple Examples
By: Jack Seymour
Update: 02/11/2023
"""

# Single Item Tuple
_t = ("delta",)
print(_t)


def do_sum(_v1, _v2):
    """
    Sum two numbers and return source and result
    """
    # Returning multiple datum as a tuple
    return (_v1, _v2, _v1+_v2)


# Automatic Tuple Unpacking
X, Y, Z = do_sum(1, 2)

print(X)
print(Y)
print(Z)
print(f"{Z} : {Y} : {Z}")

# Get the Tuple only
_t1 = do_sum(1, 2)
print(f"{_t1[0]} : {_t1[1]} : {_t1[2]}")

# Convering Lists to Tuples
_list = ["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwx", "yz"]
_tup1 = tuple(_list)  # Typecasting
_tup2 = (*_list,)  # Pointer style direct unpack
_tup3 = tuple(_v for _v in _list)  # List comprehension style
print(_list)
print(_tup1)
print(_tup2)
print(_tup3)
