word = "\t Your status: "

while True:
    found_depression = input("\n \t Do you have depression at the moment?: \n \t Type \"Yes\" if you are currently depressed \n \t Type \"No\" if you are not currently depressed \n \t Your choice: ")
    
    if found_depression == "Yes":
        status = "Poor. That's lame. If you need psychological help, you can call 911. \n"
        break
    elif found_depression == "No":
        status = "Perfect. That sounds great! \n"
        break
    else:
        print("Invalid input. Please choose either \"Yes\" or \"No\". \n")

print(word + status)
