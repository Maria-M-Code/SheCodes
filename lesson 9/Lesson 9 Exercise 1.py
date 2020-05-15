def check(s, t):
    if len(s) != len(t):
        return False
    s = sorted(s)
    t = sorted(t)

    for i in range (len(s)):
        if s[i] == t[i]:
            return True
        else:
            return False

    #     if x in t:
    #         r = True
    #         # print (r)
    #     else:
    #         r = False
    #         break
    #         # print (r)
    # return (r)


print (check('cattac', 'ctacat6'))

