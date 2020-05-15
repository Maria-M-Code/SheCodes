


array  = [i if i != 7 else 'boom'  for i in range (1,99) ]
print (array)


print (list(map(lambda i: i if i != 7 else 'boom' ,  range(1,99))))