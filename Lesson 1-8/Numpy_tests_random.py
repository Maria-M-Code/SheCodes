import numpy as np
def call():
    fields = ['fields name', 'fields some text', 'fields description']
    height = ['name', 'some text', 'description']


    np_height = np.array(height)
    np_fields = np.array(fields)


    return (np_fields + np_height)

print (call())
