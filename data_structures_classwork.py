def main():
    #problem1()
    problem2()

#PROBLEM1
#Create a function that has a loop that quits with q
#Allow the User to enter names until q is entered
#Add each name entered to a List
#When the User enters q print the list of names
#ADDITIONAL REQUIREMENTS:
#Your code should be able to process the quit command (q) the User enters regardless of case
def problem1():
    userInput = ""
    names = []
    while(userInput != "q"):
        userInput = input("Enter a name: ")
    names.append(userInput)
    print(names)

###########################################################################################################
#PROBLEM2
#Create a function that does the following when called:
#Prints a formatted list of names and ages
#Prompts the User for which property they want to use to sort the list (e.g. AGE or NAME).
#Print the formatted list of names and ages sorted by the specified sort criteria.
#Continue prompting the User for the sort criteria and print a sorted list until the User enters q then exit.

#ADDITIONAL REQUIREMENTS:
#Your code should be able to process the sort criteria the User enters regardless of case
#Your code should be able to process the quit command (q) the User enters regardless of case
#If the User enters something other than q or a valid sort criteria (e.g. AGE or NAME) your code should display INVALID ENTRY.
#PLEASE TRY AGAIN and continue the process
def problem2():
    myDictionaryList = [
        {
            "name": "Kelvin",
            "age": 30
        },
        {
            "name": "Bob",
            "age": 50
        },
        {
            "name": "Alex",
            "age": 21
        }
    ]
    userInput = ""
    while(userInput != "q"):
        for eachName in myDictionaryList:
            print(eachName)
        userInput = input("Put a string: ")





if __name__ == '__main__':
    main()