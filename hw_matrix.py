import numpy
import random
def generate_matrix(m,n):
    matrix1=[]
    for x in range(m):
        matrix2=[]
        for y in range(n):
            matrix2.append(random.randint(0,100))
        matrix1.append(matrix2)
    matrix=numpy.array(matrix1)
    return matrix
def add(A,B):
    numbersum=numpy.matrix(A)+numpy.matrix(B)
    return numbersum
def subtract(A,B):
    numbersub=numpy.matrix(A)-numpy.matrix(B)
    return numbersub
def transpose(A):
    return A.T
def dot_product(A,B):
    return numpy.dot(A,B)
def main():
    Row1=int(input('Rows in matrix A:'))
    Column1=int(input('Cols in matrix A:'))
    Row2=int(input('Rows in matrix B:'))
    Column2=int(input('Cols in matrix B:'))
    print(end='\n')
    A=generate_matrix(Row1,Column1)
    B=generate_matrix(Row2,Column2)
    print('A:\n',A)
    print('B:\n',B)
    usernum=0
    while usernum!=6:
        print('\n1. Calculate A+B')
        print('2. Calculate A-B')
        print('3. Calculate transpose of A')
        print('4. Calculate transpose of B')
        print('5. Calculate A dot B')
        print('6. Quit')
        usernum=int(input('Your choice:'))
        print(end='\n')
        if usernum==1:
                print(add(A,B))
        elif usernum==2:
                print(subtract(A,B))
        elif usernum==3:
                print(transpose(A))
        elif usernum==4:
                print(transpose(B))
        elif usernum==5:
                print(dot_product(A,B))
        elif usernum==6:
                print('Bye!')
        else:
                print('Needs integer between 1 and 6')
               
