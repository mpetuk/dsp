import numpy
A = numpy.mat([[1,2,3],[2,7,4]])
B = numpy.mat([[1,-1],[0,1]])
C = numpy.mat([[5,-1],[9,1],[6,0]])
D = numpy.mat([[3,-2,-1],[1,2,3]])
u = numpy.array([6,2,-3,5])
v = numpy.array([3,5,-1,4])
w = numpy.array([1,8,0,5]).T


print (u+v) #[ 9  7 -4  9]
print (u-v) #[ 3 -3 -2  1]
print (5*u) #[ 30  10 -15  25]
print (u*v) #[18 10  3 20]

from numpy import linalg as LA

print (LA.norm(u)) #8.60232526704

#print (numpy.add(A,C)) 
#ValueError: operands could not be broadcast together with shapes (2,3) (3,2)

print(numpy.subtract(A,C.T)) 
#[[-4 -7 -3]
# [ 3  6  4]]

print(numpy.add(C.T,3*D))
#[[14  3  3]
# [ 2  7  9]]

print(B @ A)
#[[-1 -5 -1]
# [ 2  7  4]]

#print(B @ A.T)
#ValueError: shapes (2,2) and (3,2) not aligned: 2 (dim 1) != 3 (dim 0)

#print (B @ C)
#ValueError: shapes (2,2) and (3,2) not aligned: 2 (dim 1) != 3 (dim 0)

print (C @ B)
#[[ 5 -6]
# [ 9 -8]
# [ 6 -6]]

print (B @ B @ B @ B)
#[[ 1 -4]
# [ 0  1]]

print (A @ A.T)
'''[[14 28]
 [28 69]]'''

print (D.T @ D)
'''[[10 -4  0]
 [-4  8  8]
 [ 0  8 10]]
'''
