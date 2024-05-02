'''
write a python program to compute folowing computation on matrix

1]additon of two martices
2]substraction of two matrices
3]multiplication of two matrices
4]transpose of a matrix
'''
#-----------------------------------------------------------------------------------

R=int(input("Enter no of rows:"))
C=int(input("Enter no of cloumns:"))

matrix1=[]
matrix2=[]
result = []
#-----------------------------------------------------------------------------------

for i in range (R):          
    a =[]
    for j in range(C):      
        a.append(0)
    result.append(a)    
#-----------------------------------------------------------------------------------

print("Enter the entries of 1st matrix rowwise:")
for i in range(R):     
    a =[]
    for j in range(C):      
         a.append(int(input()))
    matrix1.append(a)    
#-----------------------------------------------------------------------------------
#   
print("Enter the entries of 2nd matrix rowwise:")
for i in range(R):          
    a =[]
    for j in range(C):      
         a.append(int(input()))
    matrix2.append(a)
#-----------------------------------------------------------------------------------

#Addition of matrix
print("Addition of 2 matrix is: ")    
for i in range(len(matrix1)):  
    for j in range(len(matrix1[0])):
        result[i][j] = matrix1[i][j] + matrix2[i][j]
for r in result:
    print(r)
#-----------------------------------------------------------------------------------

#Substraction of matrix    
print("Substraction of 2 matrix is: ")    
for i in range(len(matrix1)):  
    for j in range(len(matrix1[0])):
        result[i][j] = matrix1[i][j] - matrix2[i][j]
for r in result:
    print(r)
#-----------------------------------------------------------------------------------

#multiplication if matrix    
print("multiplication of 2 matrix is: ")

for i in range(len(matrix1)):
   for j in range(len(matrix2[0])):        # iterate through columns of Y
       for k in range(len(matrix2)):       # iterate through rows of Y
           result[i][j] += matrix1[i][k] * matrix2[k][j]
for r in result:
   print(r)
#-----------------------------------------------------------------------------------
 
#Transpose of matrix   
print("Transpose of matrix 1 is: ")
for i in range(len(matrix1)):
   # iterate through columns
   for j in range(len(matrix1[0])):
       result[j][i] = matrix1[i][j]

for r in result:
   print(r)
print("Transpose of matrix 2 is: ")
for i in range(len(matrix1)):
   # iterate through columns
   for j in range(len(matrix2[0])):
       result[j][i] = matrix2[i][j]

for r in result:
   print(r)


