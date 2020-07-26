# def Sort_Tuple(newlist):  
  
#     # reverse = None (Sorts in Ascending order)  
#     # key is set to sort using second element of  
#     # sublist lambda has been used  
#     newlist = sorted(newlist, key=lambda k: k['overlInf'], reverse=False)
#     return newlist  
  
# # Driver Code  
# newlist = [{'OverlInf': 'מהנדס/ת (מחקר)', 'field': 'שם עיסוק'}
# , {'OverlInf': 'מזכיר ראשון (מנהלה)', 'field': 'שם עיסוק'}
# , {'OverlInf': 'יועץ (ש.מ.)', 'field': 'שם עיסוק'}
# , {'OverlInf': 'מנהל כללי', 'field': 'שם עיסוק'}
# , {'OverlInf': 'סטודנט/ית', 'field': 'שם עיסוק'}
# , {'OverlInf': 'סטודנט', 'field': 'שם עיסוק'}
# ]
  
# # printing the sorted list of tuples 
# print(Sort_Tuple(newlist)) 

import collections

print ('dict       :'),
d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'
d1['d'] = 'D'
d1['e'] = 'E'

d2 = {}
d2['e'] = 'E'
d2['d'] = 'D'
d2['c'] = 'C'
d2['b'] = 'B'
d2['a'] = 'A'

print (d1 , d2)

print ('OrderedDict:'),

d1 = collections.OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'
d1['d'] = 'D'
d1['e'] = 'E'

d2 = collections.OrderedDict()
d2['e'] = 'E'
d2['d'] = 'D'
d2['c'] = 'C'
d2['b'] = 'B'
d2['a'] = 'A'

print (d1 , d2)