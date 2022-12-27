#this is to reverse digits
def reversedigits(num):
    rev = 0
    while (num > 0 ):
        rev = rev * 10 + num % 10
        num //= 10

    return rev

#here numbers are squared
def square(num):
    return (num *num)


#checking adam number or not
def checkAdamNumber(num):
    
    a = square(num)
    b = square(reversedigits(num))

    if (a == reversedigits(b)):
        return True

    else :
        return False



num = int(input("Enter the number to be checked :"))

if(checkAdamNumber(num)):
    print('yes',num, 'is a Adam Number')

else :
    print ("Not a Adam Number")
    
    
