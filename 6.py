'''

Write python program to store first year percentage of students
in array. Write function for sorting array of floating point numbers in ascending order using
quick sort and display top five scores.

'''

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1
def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

list=[]
n=int(input("Enter the no of elements :"))
print("Enter scores of ",n," students:")
for i in range(0,n):
    a=int(input())
    list.append(a)
print(list)    
print("Unsorted Array")
print(list)
size = len(list)
quickSort(list, 0, size - 1)
print('Sorted Array in Ascending Order:')
print(list)

print("Top 5 scorers:")
print(list[n-5:n])
