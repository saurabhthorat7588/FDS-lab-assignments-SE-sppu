'''Write Pythin program to store marks scored for
first test of sub DSA for n students.
Compute
A.Average score of class.
B.Heighest and lowest score of class.
C.Marks scored by most of the studetns.
D.List of students who were absent for the test. 
'''

#Marks input
MarksinFDS=[]
n=int(input("ENter number of students in class:"))
for i in range(n):
    marks=int(input("Enter marks for student "+str(i+1)+" :"))
    MarksinFDS.append(marks)

#avg score of class
def average(listofmarks):
    sum=0
    count=0
    for i in range(len(listofmarks)):
        if listofmarks!=-999:
            sum=sum+listofmarks[i]    
            count=count+1
        avg=sum/count
    print("The sum of all marks is:",sum)    
    print("The avg of all marks is:",avg)

#Heighest and Lowest score of class
def Hscore(listofmarks):
    for i in range(len(listofmarks)):
        if listofmarks!=-999 :
            Max=listofmarks[0]
            break     
    for i in range(1,len(listofmarks)):
        if listofmarks[i]>Max :
            Max=listofmarks[i]
    return(Max)

def Lscore(listofmarks):
    for i in range(len(listofmarks)):
        if listofmarks!=-999:
            Min=listofmarks[0]
            break
    for i in range(1,len(listofmarks)):
        if listofmarks[i]<Min:
            Min=listofmarks[i]
    return(Min)

#Marks scored by most of the students                
def maxFrequency(listofmarks):
    i=0
    max=0
    print("Marks | Frequuency")
    for j in listofmarks:
        if (listofmarks.index(j)==i):
            print(j,"   |   ",listofmarks.count(j))
            if listofmarks.count(j)>Max:
                Max=listofmarks.count(j)
                mark=j
        i=i+1
    return(mark,Max)

#Absent students
def absent(listofmarks):
    count=0
    for i in range(len(listofmarks)):
        if(listofmarks[i]==-999):
            count+=1
    return(count)      


#Function for continue
def Continue():
    a=str(input("\nDo you want to continue(Yes/No):"))
    if(a=="Yes"):
        flag=1
    elif(a=="No"):
        flag=0
        print("Thanks fo using the program:")
    return(0)

#Menu
flag=1
while(flag==1):
    print("\n---------------------------*****---------------------------")
    print("1] Average score of class:")
    print("2] Heighest and lowest score of class:")
    print("3] Max freaquency of class:")
    print("4] Number of absent students:")
    print("\n---------------------------*****---------------------------")

    ch=int(input("Enter yout choice:(1-5)"))
    if ch==1:
        average(MarksinFDS)
        Continue()
    
    if ch==2:
        print("The heighest score in the class is:",Hscore(MarksinFDS))
        print("The Lowest score in the class is:",Lscore(MarksinFDS))
        Continue()

    if ch==3:
        mark,fr=maxFrequency(MarksinFDS)
        print("heighest frequency of mark {0} that is {1}",format(mark,fr))    
        Continue()

    if ch==4:
        print("The number absent students is:",absent(MarksinFDS))
        Continue()
    


    
    



