import cmath

a = 1
b = 2
c = 3

#Discriminant calculation

d = (b**2) - (4*a*c)

#calculate square root using cmath

sol1 = -b-cmath.sqrt(d)/(2*a)
sol2 = -b+cmath.sqrt(d)/(2*a)

print("The solutions are {0} and {1}".format(sol1,sol2))