x = int(input('Enter x cordinates of reference point :'))
y = int(input ('Enter y cordinates  of reference point'))
no_of_input = int(input('Enter the total point'))


list1 = []
for number in range(no_of_input):
    x1 = int(input('Enter x cordinates  :'))
    y1 = int(input ('Enter y cordinates :'))
    merge = (x1,y1)
    list1.append(merge)
print(list1)
#         x1,y1    x2,y2
list1 = [(1, 1), (-1, -1)]

eucledian_distence = (list1[1][0]-list1[0][0])**2 + (list1[1][1]-list1[0][0])**2
#ucledian_distance =  (((x-i)**2 + (y-j)**2))  #( x2 − x1 )2 + ( y2 − y1 )2
print(eucledian_distence)
