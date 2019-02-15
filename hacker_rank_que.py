if __name__ == '__main__':
    n = int(input())  # number
    student_marks = {}  # dictionary
    for _ in range(n):  # number of inputs
        l = input().split()  # convert into list
        scores = list(l[1:])  #
        name = l[0]
        del l
        scores = list(map(float, scores))
        student_marks[name] = scores
    query_name = input()

    print("{:.2f}".format(sum(student_marks[query_name]) / len(student_marks[query_name])))