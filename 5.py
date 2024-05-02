'''

Write a python program to store roll no.s of students in array who attended
training program in random order. Write function for seaching whether particular
student attended training program or not using  linear search and sentinal search.

'''
# Linear and Sentinal Search
def linear_search(RollNo,key):
    for i in range(len(RollNo)):
        if RollNo[i]==key:
            return i
    return "Not Found"

def sentinal_search(RollNo,key):
    if key==(len(RollNo)-1):
        return(len(RollNo)-1)

    for i in range(len(RollNo)):
        if RollNo[i]==key:
            return i
    return "Not Found"

RollNo=input("Enter the Roll numbers of the students(Give space between entries:):\n")
RollNo=RollNo.split()
RollNo=[int(x) for x in RollNo]
key=int(input("Enter the number to search for:\n"))
index = sentinal_search(RollNo,key)
index1= linear_search(RollNo,key)
print("Index for Sentinal:",key,"is at",index,"position")
print("index for linear:",key,"is at",index1,"position")
