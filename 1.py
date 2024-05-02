'''Write Pythin program to store marks scored for
first test of sub DSA for n students.
Compute
A.Average score of class.
B.Heighest and lowest score of class.
C.Marks scored by most of the studetns.
D.List of students who were absent for the test. 
'''
# List of marks input
marksinFDS = []
no_ofstudents = int(input("Enter no of students:"))
for i in range(no_ofstudents):
    marks = int(input("Enter marks of student "+str(i+1)+":"))
    marksinFDS.append(marks)
# -----------------------------------------------------------------------------------

# Function for avg marks


def average(listofmarks):
    sum = 0
    count = 0
    for i in range(len(listofmarks)):
        if listofmarks != -999:
            sum += listofmarks[i]
            count += 1
        avg = sum/count
    print("Total Marks: ", sum)
    print("Avg Score: {:.2f}".format(avg))
# -----------------------------------------------------------------------------------

# Function for Heighest score in the test of the class


def Max(listofmarks):
    for i in range(len(listofmarks)):
        if listofmarks != -999:
            Max = listofmarks[0]
            break
    for i in range(1, len(listofmarks)):
        if listofmarks[i] > Max:
            Max = listofmarks[i]
    return (Max)
# -----------------------------------------------------------------------------------

# Function for Lowest score in the test of the class


def Min(listofmarks):
    for i in range(len(listofmarks)):
        if listofmarks != -999:
            Min = listofmarks[0]
            break
    for i in range(1, len(listofmarks)):
        if listofmarks[i] < Min:
            Min = listofmarks[i]
    return (Min)
# -----------------------------------------------------------------------------------

# Function for counting the number of students absent for the test


def absent(listofmarks):
    count = 0
    for i in range(len(listofmarks)):
        if listofmarks[i] == -999:
            count += 1
    return (count)

# -----------------------------------------------------------------------------------

# Function for displaying marks with heighest frequency


def maxFrequency(listofmarks):
    i = 0
    max = 0
    print("Marks | Frequuency")
    for j in listofmarks:
        if (listofmarks.index(j) == i):
            print(j, "   |   ", listofmarks.count(j))
            if listofmarks.count(j) > Max:
                Max = listofmarks.count(j)
                mark = j
        i = i+1
    return (mark, Max)
# -----------------------------------------------------------------------------------


# MENU
flag = 1
while flag == 1:
    print("\n______________________________________****____________________________________________")
    print("\n1] Press 1 for Avg score of class:")
    print("\n2] Press 2 for Heighest and lowest score of class:")
    print("\n3] Press 3 for no of absent students of class:")
    print("\n4] Press 4 for Heighest frequency of marks:")
    print("\n5] Press 5 to exit :")
    print("\n______________________________________****____________________________________________")

    ch = int(input("\nEnter your choice(1-5): "))
    if ch == 1:
        average(marksinFDS)
        a = str(input("\nDo you want to continue(yes/no):"))
        if (a == "yes"):
            flag = 1
        elif (a == "no"):
            flag = 0
            print("Thanks fo using the program:")
    if ch == 2:
        print("The heighest score in class is ", Max(marksinFDS))
        print("The heighest score in class is ", Min(marksinFDS))
        a = str(input("Do you want to continue(yes/no)?"))
        if (a == "yes"):
            flag = 1
        elif (a == "no"):
            flag = 0
            print("Thanks fo using the program:")
    if ch == 3:
        print("The number of absent students for the test is: ", absent(marksinFDS))
        a = str(input("Do you want to continue(yes/no)?"))
        if (a == "yes"):
            flag = 1
        elif (a == "no"):
            flag = 0
            print("Thanks fo using the program:")
    if ch == 4:
        mark, fr = maxFrequency(marksinFDS)
        print(
            "Heighest frewuency os of mark {0} that is {1} ", format(mark, fr))
        a = str(input("Do you want to continue(yes/no)?"))
        if (a == "yes"):
            flag = 1
        elif (a == "no"):
            flag = 0
            print("Thanks fo using the program:")
    elif ch == 5:
        flag = 0
        print("Thanks for using the program!")
    else:
        print("Wrong choice!")
        a = str(input("Do you want to continue(yes/no)?"))
        if (a == "yes"):
            flag = 1
        elif (a == "no"):
            flag = 0
            print("Thanks fo using the program:")
