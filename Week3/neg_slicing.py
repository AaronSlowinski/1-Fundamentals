my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Using negative indices for start and stop
slice1 = my_list[-5:-2]
print("Slice with negative start and stop:", slice1)  # ['c', 'd', 'e']

# Using a negative step to reverse the sequence
slice2 = my_list[::-1]
print("Sequence reversed using negative step:", slice2)  # ['g', 'f', 'e', 'd', 'c', 'b', 'a']

# Combining negative start, stop, and step
slice3 = my_list[-2:-5:-1]
print("Combining negative start, stop, and step:", slice3)  # ['f', 'e', 'd']
