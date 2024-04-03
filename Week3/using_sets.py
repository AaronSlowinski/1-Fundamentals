#number_set = {1,2,3,4,(5,6,7,8,9,10)}
#print(number_set)

words_set = {"apple", "banana", "cherry", "date", "elderberry"}
"""abcd="" 
for word in words_set:
    abcd+=word
print(abcd)
"""

"""if "apple" in words_set:
    print("apple is in the set")
else:
    print("apple is not in the set")
    """

words_set.add("fig")
print(words_set)
words_set.discard("banana")
print(words_set)