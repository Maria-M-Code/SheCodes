def Sort_Tuple(tup):
    # reverse = None (Sorts in Ascending order)
    # key is set to sort using second element of
    # sublist lambda has been used
    # tup.sort(key=lambda x: x[1]
    # newlist = sorted(tup, key=lambda k: k['OverlInf'], reverse=False)
    newlist = sorted(tup, key=lambda k: (k['ddd'], k['OverlInf']), reverse=False)

    return newlist


# Driver Code
tup = [{'OverlInf': 'מהנדס/ת (מחקר)', 'field': 'שם עיסוק' , 'ddd': 2}
    , {'OverlInf': 'מזכיר ראשון (מנהלה)', 'field': 'שם עיסוק', 'ddd':2}
    , {'OverlInf': 'יועץ (ש.מ.)', 'field': 'שם עיסוק', 'ddd': 1}
    , {'OverlInf': 'מנהל כללי', 'field': 'שם עיסוק', 'ddd': 1}
    , {'OverlInf': 'סטודנט/ית', 'field': 'שם עיסוק', 'ddd': 2}
    , {'OverlInf': 'סטודנט', 'field': 'שם עיסוק', 'ddd': 2}
       ]

# printing the sorted list of tuples
print(Sort_Tuple(tup))
