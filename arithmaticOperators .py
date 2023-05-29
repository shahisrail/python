# Arithmatic Operators 
# a = 100
# b = 100
# print('a+b = : ', a+b)

# input => return string 

# a = input("Enter a Number")
# print(type(a))

a = int(input('Enter first Number : '))
b = int(input('Enter 2nd Number : '));
c = int(input('Enter third Number : '))

# print('{}'.format(a))
# arithSummation = a + b + c
# print("Summation of 3 numbers : ", arithSummation);
# print("Summation of a : {} b : {} c :{}" .format(a,b,c),arithSummation)
print('Summation of a: {} b : {} c : {}'.format(a,b,c),a+b+c)
print('Subtraction of a: {} b {} c : {}'.format(a,b,c),a-b-c)
print('Multiplication of a: {} b: {} c :{}'.format(a,b,c),a*b*c)
print('Division of a: {} b: {} c: {}'.format(a,b,c),a / b / c) # float value
print('Floor Division of a: {} b: {}'.format(a,b,c),a // b)
print('Exponent a: {} b: {}'.format(a,b),a ** b)
print('Exponent a: {} b: {}'.format(a,b),a % b)


# / operator always performing floting arithmatic. It always return float value.a
# But Floor Division // opertor can perform both floating Point & integral (integer)
# arithmatic
# if arguments are  int types result will int type.
# if atleast one argument is float type than result is float.

# Example :

aa = 10
bb = 2
print(aa / bb)
print(aa // bb)


# Note :  
# We can use + , * operators for str type.
# if we want to use + operator for str type then compulsary both arguments
# should be str type only otherwise we will get error.

# Example:
# print('Mahbub' + 10) #TypeError
print('Mahbub'+'10')

# if we want to use * operator for str type then compulsary one arguments
# should be int type 2nd argument should be str.

print(2 * 'Mahbub') 

# note: 
# + => String Concatenation Operator
# * => String Multiplication Operator 
