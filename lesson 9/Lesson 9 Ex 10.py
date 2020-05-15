joules = ['HTML', 'Phyton','HTML', 'Phyton']
# res = [i for i in joules if i !='Phyton' ]


# def my_course(current):
#     return current =='Phython'

res =  list(map(lambda i:i  , filter(1==1, joules)))
print (res)