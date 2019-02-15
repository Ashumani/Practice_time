if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a, b)
    for i in range(a):
        for j in range(b):
            if (i+j) %2 == 0:
                print('*', end="")
            else:
                print('.', end="")
        print()
