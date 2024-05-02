a=[5,4,6,3,7,2,9,8]
def sel(a):
    for i in range(len(a)):
        min=i
        for j in range(i+1,len(a)):
            if a[min]>a[j]:
                min=j
        a[i],a[min]=a[min],a[i]
    print(a)
sel(a)

def partition(a,low,high):
    pivot=a[high]
    i=low-1
    for j in range(low,high):
        if(a[j]<=pivot):
            i=i+1
            (a[i],a[j])=(a[j],a[i])
    (a[i+1],a[high])=(a[high],a[i+1])
    return i+1

def qs(a,low,high):
    if low<high:
        pi=partition(a,low,high)
        qs(a,low,pi-1)
        qs(a,pi+1,high)