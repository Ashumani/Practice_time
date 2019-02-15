a=open("input2.txt","r")
dict={}
list=[]
list1=[]
for i in a:
	list.append(i)
print(list)
for j in list:
	d=j.split(" ")
	print(d)
	dict["DOB"]=d[0]
	dict["name"]=d[1]
	dict["age"]=d[2]
	print(dict)
	dict={} #its not displaying all records
	# print(dict)
	# print (j)
	list1.append(dict[j])
	#dict={}  #for blank the dictionary for next data
print(list1)