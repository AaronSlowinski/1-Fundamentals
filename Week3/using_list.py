states = ["Washington", "Oregon", "California"]

""""
print(states[-1])
print(states[-2])
print(states[-3])
"""

states[2] = "Arizona"
# print(states)

#len(states) gets the length of the list
#print(len(states))

states.append("New York")
print(states)

states.pop()
print(states)

states.pop(1)
print(states)
