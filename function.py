
# def larger(num1, num2):
#     if num1 > num2:
#         return num1
#     return num2
#
#
# def largest(a, b, c):
#     large = larger(a, b)
#     return larger(large, c)
#
# print(largest(3, 4, 5))

n = int(input('enter the no to check prime or not :'))


def prime(a):
    for j in range(2, a):
        if a % j == 0:
            return False
    return True


for i in range(2, n):
    if prime(i):
        print(f"{i} is prime")
    else:
        print(f"{i} is not prime")






