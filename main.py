a = []
b = input("Type 'yes' to start inputting numbers: ")
c = 0
n = 0

while b.lower() == 'yes':
    d = int(input("Enter a number to calculate the average: "))
    if d not in a:
        a.append(d)
        c += d
        n += 1
        e = c / n
        print("The new average is", e)
        b = input("Do you want to continue?(Yes/No) ").lower()
    else:
        print("Number already exists. Type a new number.")
        continue
if b.lower()!='yes':
    print("Thank you for using the program")