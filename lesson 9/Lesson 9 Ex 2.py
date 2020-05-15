list1 = ['1' , '2', '3','4' , '5', '6']
list2 = ['A' , 'B', 'C', 'D', 'E', 'F']
array = {list1[x]: list2[x] for x in range(len(list2)) if x!= 4}

print (array)

