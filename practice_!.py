# for i in range  (10):
#     print(i,end=' ')
#     print(i,sep='*')

student={}

n = int(input())
for i in range(n):
    c = input()
    a = c.split()
    b = a[1:]
    name = a[0]

    student[name] = b
query = input()
value = student.get(query)
list1=list(map(int,value))
result = sum(list1)/len(list1)
print("{:.2f}".format(result))

