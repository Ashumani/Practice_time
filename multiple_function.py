# user = input()
def userinput(user):
    tuple1=()
    for i in range(user):
        first_name = input("name :")
        last_name= input("lastname :")
        mobileno= input("mobileno :")
        profession= input("profession :")
        list1=tuple(first_name,last_name,mobileno,profession)
    print(list1)


userinput(10)