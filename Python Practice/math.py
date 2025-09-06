from  import *
x,y,z=symbols('x y z')
A=Matrix([[1,-1,1],[3,-1,2],[3,1,1]])
B=Matrix([[2],[-6],[-18]])
n=A.shape[1]
AB=A.col_insert(n,B)
eAB=AB.echelon_form()
rA=A.rank()
rAB=AB.rank()
print('The rank of coefficient matrix ',rA)
print('The rank of Augmented matrix ',rAB)
if rA==rAB:
    if rA==n:
        print('The system is consistent and has unique solution')
    else:
        print('The system has infinitely many solutions')
else:
    print("The system is inconsistent")
sol=solve_linear_system(AB,x,y,z)
display(sol)
