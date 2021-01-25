list1 = [1,2,3,4,5]

list2 = ['a','b','c','d','e']

print("list1 is :" +str(list1))

print("list2 is :" +str(list2))

res = {}

for keys in list1:

    for value in list2:

        res[keys]=value
        list2.remove(value)
        break

print("dictionary is :" +str(res))               
