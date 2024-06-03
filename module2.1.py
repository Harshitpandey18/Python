def collatz(number): #A function is created
    if number%2==0: #if condition is checked
        return number//2
    else: 
        return 3*number+1
number=int(input("Enter any Number: ")) #takes user input
a=collatz(number) #'a' is assigned with the value of function
while collatz(number)!=1: #while loop will run till function is not equals 1
    print(a)
    a=collatz(a) #a new value is assigned to 'a'
    if a==1: #checks if condition is true
        break 
    
