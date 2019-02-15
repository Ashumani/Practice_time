if __name__ == '__main__':
    num=[1,2,3,4,5]
    # square_of_number=[]
    # for i in num:
    #     square_of_number.append(i**2)
    # print(square_of_number)


    #
    # result=[(i**2) for i in num]
    # print(result)


    # def cube(value):
    #     return (value ** 3)
    #
    #
    # # result1 = [(i ** 2) for i in num if (i%2==0)]
    # # print(result1)
    # result1 = [cube(i) for i in num if (i%2==0)]
    # print(result1)

    # for i, j in enumerate(num) :
    #     print(i,j)

    # how to take multiple input using map
    # x, y, z, n=list(map(int, input().split()))
    # print(x,y,z,n)

    #use multiple value using list Comphression
    # x,y,z,n=[int(i) for i in input().split()]
    # print(x,y,z,n)
    def value2(value):
        return value**2

    ans={ key:value2(value) for key,value in enumerate(num)}
    print(ans)