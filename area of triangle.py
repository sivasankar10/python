#area triangle

a = float(input("Enter the first side : "))
b = float(input("Enter the second side : "))
c = float(input("Enter the third side : "))

#calaculating the semiperimeter

s = (a + b + c )/ 2



#calculate area
area = (s*(s-a)*(s-b)*(s-c))**0.5

print('The area of the triangle is %0.2f'%area)
