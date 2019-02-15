'''

A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
Syntax:
        lambda arguments : expression

'''
x = lambda a : a + 10
print(x(5))  # Output = 15

x = lambda a, b : a * b
print(x(5, 6))  # Output = 30

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))  # Output = 13

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))  # Output = 22


def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)
print(mytripler(11))  # Output = 33



def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11)) # Output = 22 33