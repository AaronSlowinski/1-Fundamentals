while True:
    print ("1. Number One ")
    print ("2. Number Two ")
    print ("3. Break out of infinite loop ")
    option = input("Enter your option: ")
    if option == "1":
        print ("You chose option 1")
    elif option == "2":
        print ("You chose option 2")
    elif option == "3":
        print ("You chose option 3")
        break
    else:
        print ("Invalid option")
print ("You have left the infinite loop.")