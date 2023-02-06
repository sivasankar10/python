import cmath

a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
c = int(input("Enter the value of c : "))


discriment = (b**2) - (4*a*c)


sol1 = (-b-cmath.sqrt(discriment))/(2*a)
sol2 = (-b+cmath.sqrt(discriment))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))
