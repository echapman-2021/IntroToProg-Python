# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# EChapman,2.10.2021,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = open("C:\_PythonClass\Assignment05\ToDoList.txt","r")  # An object that represents a file
strData = ""
task = ""
priority = ""
dicRow = {task: priority}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []
strMenu = """
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """
strChoice = "" # A Capture the user option selection
# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
for dicRow in objFile:
    dicRow = dicRow.strip()
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print(strMenu)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print("\n")
    if (strChoice.strip() == '1'):
        print("<Current Data>")
        for i in lstTable:
            print(i)
        continue
    #Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        task = str(input("Enter a Task: "))
        priority = str(input("Enter a priority: "))
        dicRow = {task: priority}
        lstTable.append(dicRow)
        for i in lstTable:
            print(i)
        continue
    #Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        print(lstTable)
        task_to_remove = input("Select the a task to remove...Be Specific: ")
        if task_to_remove in lstTable:
            lstTable.remove(task_to_remove)
            print("{", task_to_remove, "} has been deleted")
        else:
            print("Task doesn\'t exist")
        continue
    # Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        print("Would you like to save your ToDO?")
        y_or_n = input("Enter y or n: ")
        if y_or_n == "y":
            objFile = open("C:\_PythonClass\Assignment05\ToDoList.txt", "a")
            objFile.write(task + ":")
            objFile.write(priority + "\n")
            print("Data saved to file")
            objFile.close()
            continue
        else:
            continue

    elif (strChoice.strip() == '5'):
        print("Exiting program...", "\nGoodbye")
    break
