#save data in file
# def save_data(name, age, mobileno):
#     file = open("input2.txt", "w")
#     data = "Name: {}, age = {}, mobileno ={}".format(name, str(age), str(mobileno))
#     file.write(data)
#     file.close()

# def save_data(*args):
#     file = open("input2.txt", "w+")
#     data = "Name: {}, age = {}, mobileno ={}".format(*args)
#     file.write(data)
#     file.close()
    # print(data)

# def save_data2(**kwargs):
#     data = ""
#     for i, j in kwargs.items():
#         # print(i, str(j))
#         data = data + "{}: {} ".format(i, str(j))
#     file = open("input2.txt", "w")
#     file.write(data)
#     file.close()

def save_both_data( *args , **kwargs):
    kwargsdata = ""
    argsdata =""
    file=open("input2.txt", "w+")
    for i in args:
        argsdata += "{}".format(i)
        print(argsdata)


    for i,  j in kwargs.items():
        kwargsdata=kwargsdata + "{}, {} ".format(i, str(j))
    print(kwargsdata)
    file.write(argsdata)
    file.write(kwargsdata)
    file.close()


lis = list(range(1, 5)) # list
tup = tuple(range(1, 5)) # tuple

dic = {i:j for i,j in enumerate(list(range(1, 5)))}


