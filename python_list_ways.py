my_list = []
my_list1 =[1,2,3]
my_list2 = [1,2,"manish",4]
my_list3= ["mouse", [8, 4, 6], ['a']]
print(my_list , my_list1,my_list2)
print(my_list3)

my_list = ['p','r','o','b','e']
# Output: p
print(my_list[0])

# Output: o
print(my_list[2])

# Output: e
print(my_list[4])

# Error! Only integer can be used for indexing
# my_list[4.0]

# Nested List
n_list = ["Happy", [2,0,1,5]]
print(n_list[0][1])
print(n_list[1][0])
print(n_list[1][3])

my_listt = ['p','r','o','b','e']
print(my_listt[1])
print(my_listt[-1])
print(my_listt[-5])
print(my_listt[2:4])
print(my_listt[:])
print(my_listt[2:])
my_listt[0]="manish"
print(my_listt)
my_listt[1:4] = [3, 5, 7, 6, 8, 9]
print(my_listt)
my_listt.append("ashish")
print(my_listt)
my_listt.extend([9, 11, 13])
print(my_listt)

# list=[1,2,3,4,5,6,]
# for i in list:
#     print(i)
#
#
# S = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# S3 ={0, 1, 4, 9, 16, 25, 36, 49, 64, 81}
# V = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
# M = [0, 4, 16, 36, 64]
# S1=[x**2 for x in range(10)]
# S2=[x**2 for x in range(10)]
# V1=[2**i for i in range(13)]
# M1= [x for x in S if x % 2 == 0]
# print(S1)
# print(V1)
# print(M1)
# print(S2)