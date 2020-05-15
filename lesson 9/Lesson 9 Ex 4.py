array  = []
for i in range (1,10):
    if i % 2 == 0:
        array.append(i*100)
print (array)

array  = [i*100  for i in range (1,10) if i % 2 == 0]
print (array)

print (list(map(lambda i: i*100,  (filter(lambda i : i % 2 == 0, range(1,10))))))

print  (list (filter(lambda i : i % 2 == 0, range(1,10))))

