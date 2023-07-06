word = " \t Hello! \n \t \t This simple script is created to allow you to make your own \"lists\" and fill them with elements. \n"
print(word)
end = 1

while end:
    list_length = int(input("\t Type length of your list: "))
    own_list = []
    i = 0 

    while i < list_length: 
        elements_string = "Type the value of element#" + str(i+1) + ": "
        own_list.append(input(elements_string))
        i += 1

    print("\n The list you created looks like this: " + str(own_list))

    while True:
        end = input("\n \t Do you want to create another list? \n \t Pick \"Yes\" or \"No\" \n \t Your choice: ")
        if end == "No":
            end = 0
            break
        elif end == "Yes":
            end = 1
            break
        else:
            print("Invalid input. Please choose either \"Yes\" or \"No\". \n")

own_list = []
i = 0 
print ("\n \t Thanks for using this script, good luck! \n")
