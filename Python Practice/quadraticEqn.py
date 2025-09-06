import cmath  
a=1
b=5
c=6

d=(b**2) - (4*a*c)
root1 = (-b-cmath.sqrt(d))/(2*a)
root2 = (-b+cmath.sqrt(d))/(2*a)

#print("the solution are {0} and {1} ".format (sol1,sol2))
print ("the roots of eqn is", root1 ,root2)