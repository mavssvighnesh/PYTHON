import numpy as np
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))


print("enter the elements of the first matrix")
matrix1 = []
print("Enter the entries rowwise:")
 
for i in range(R):         
    a =[]
    for j in range(C):    
         a.append(int(input()))
    matrix1.append(a)
print("enter the elements of the second matrix ")
matrix2 = []
print("Enter the entries rowwise:")
 
# For user input
for i in range(R):          # A for loop for row entries
    a =[]
    for j in range(C):      # A for loop for column entries
         a.append(int(input()))
    matrix2.append(a)
A=np.array(matrix1)
B=np.array(matrix2)

sum= np.add(A, B)
print("The sum of 2 matrices will be:")
print(sum)

print("the multiplication of the given arrayes is ")
A=np.array(matrix1)
B=np.array(matrix2)

mul=np.matmul(A,B)
print("The multiplication of 2 matrices will be:")
print(mul)