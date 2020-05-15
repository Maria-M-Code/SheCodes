# array  = []
# for i in range (1,10):
#     if i % 2 == 0:
#         array.append(i*100)
#     else:
#         array.append(i)
# print (array)


array  = [i*100 if i % 2 == 0 else i  for i in range (1,10) ]
print (array)

print (list(map(lambda i: i*100, list (filter(lambda i : i % 2 == 0, range(1,10))))))

print (list(map(lambda i: i*100 if i % 2 == 0 else i ,  range(1,10))))