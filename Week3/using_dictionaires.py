state_capitals = {"washington": "olympia", "oregon": "salem", "california": "sacramento"}
# print (len(state_capitals))

#print (state_capitals["washington"])
state_capitals["washington"] = "Aberdeen"
state_capitals["texas"] = "Austin"

print (state_capitals)

del state_capitals["california"]

print (state_capitals)

state_capitals.pop("oregon")
print (state_capitals)


