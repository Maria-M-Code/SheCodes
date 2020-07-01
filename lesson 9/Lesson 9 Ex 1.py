movie = ['The NoteBook' , 'Laleficent', 'Batman v Superman']
actor = ['rachel McAdams', 'Angelina Jolie', 'Gal Badot']

out  = [(str(k) + ' is played by ' + str(v)) for (k, v) in zip(movie, actor)]
print(out)
print(out)
