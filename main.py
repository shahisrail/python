# bool 

'''True  = > 1
False =>  0
'''
#usecase True (1) False (0)

# fisrtName = input("Enter Your Name  ")

# if fisrtName == 'Mahbub':
#     print("Your Name is ",fisrtName)

# mahbub = False (0)
# test = True (1)

# test = 1
# # print(mahbub)
# print(test)



# Type Casting 
#  We can convert one type value to another type value. 
# This conversion is called TypeCasting 
#  or Type coersion. 

# The Following are varuious inbuilt functions for type casting
# 1.int()
# 2.float()
# 3.complex()
# 4.str()
# 5.bool()


# int(): we can use this function to convert values from other types

# float to int 
a = 10.222
print(int(a)) # 10

#complex to int 
# b = 10+5j
# print(int(b))  # TypeError can't convert complex to int
# print(type(b))

# bool to int 
boo = True
foo = False
print(int(foo))
print(int(boo))
#print(boo)

# st ='10'
# st11 = '1.25'
# print(int(st11))
# st ='Mahbub'
# print(st)
# print(int(st)) 


# Note:
# We can convert from any type to int except compplex type
# If we want to convert str type to int type, 
# compulsary str should contain only integral value 
# and should be specified in base-10 


# float() : we can use float() this function to convert values from other types
# int to float 
ii = 10
print(float(ii)) 


#complex to float 
# b = 10+5j
# print(int(b))  # TypeError can't convert complex to float
# print(type(b))


# bool to float 
boo = True
foo = False
print(float(foo))
print(float(boo))
#print(boo)


# complex() : we can use complex() this function to convert values from other types

# com = a + 10j 
#  a = real part 
#  10j = imiginary part

# int to complex
intValue = 100 # real part
print(complex(intValue)) #(100+0j) 0j=> imiginary part

# float to complex
floatVlaue = 10.25
print(complex(floatVlaue)) #(10.25+0j)

# bool to complex
bol = True
bol3 = False
print(complex(bol)) #(1+0j)
print(complex(bol3)) #(0j)

# string to complex 
strr = 'ten'
str22 = '10.255'
#print(complex(strr)) #complex() arg is a malformed string
print(complex(str22)) #(10+0j)


# bool() : we can use bool() this function to convert values from other types
aaaaa = 10
aaaaass = 0
flbol = 10.55
fbol2 = 0.0
strbol = 'Hello World'
strbol11 = ''
print(bool(strbol11))
print(bool(strbol))
print(bool(fbol2))
print(bool(flbol))
print(bool(aaaaa))
print(bool(aaaaass))
