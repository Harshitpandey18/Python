import random #random module is imported
for i in range(1000): #this experiment will run 1000 times
    List=[] #empty list
    totalH=0
    totalT=0
    hstreak=0
    tstreak=0
    n=int(input("How many times do you want to toss?: ")) #takes input from user
    for j in range(1,n+1): 
        x=random.randint(0,1) #gives random number
        if x==0:
            List.append('H') #appends the list
        else:
            List.append('T') #appends the list
    print("The list is: \n",List) 
    for k in List: #loop will run in list
        if k=='H': 
            totalH +=1 #totalH is incremented
            if totalH==6:
                hstreak +=1 #hstreak is incremented 
        else:
            totalH=0
    for l in List: 
        if l=='T':
            totalT +=1 #totalT is incremented
            if totalT==6:
                tstreak +=1 #tstreak is incremented 
        else:
            totalT=0
    print("Count of streak of Heads is: ",hstreak) #statements will be printed
    print("Count of streak of Tails is: ",tstreak)

