a = []  # a is a list to store all the new elements that will be
# inputted by the user
b = input("Type 'yes' to start inputting numbers: ")
# b is a identifier for a string
# it is to check if the user wants to start the program
c = 0  # c is to calculate the sum of newly inputted numbers by the user
n = 0  # n is to calculate the total number of newly added elements

while b.lower() == 'yes':  # starts a loop if the user wants to continue with the program
    d = int(input("Enter a number to calculate the average: "))  # d points to the inputted number
    if d not in a:  # if the inputted number is not in the list it is considered as a new element
        # and continues with rest of code below
        a.append(d)  # adds number to the list
        c += d  # calculate the total sum
        n += 1  # total numbe of new elements
        e = c / n  # calculates the average
        print("The new average is", e)  # prints the average
        b = input("Do you want to continue?(Yes/No) ").lower()  # checks if user wants to continue
    else:  # this condition is satisfied only when the number entered by the user is already been inputted
        print("Number already exists. Type a new number.")  # prints the message
        print(e)  # prints the last average
        continue
if b.lower() != 'yes':  # either in the beginning or in between the loop if they want to exit the program
    # they have to type something other than 'yes'
    print("Thank you for using the program")  # print[[[23s in the  end of the program
