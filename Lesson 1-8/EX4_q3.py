

def try_again():
    i = 1
    while i <= 27:
        if i % 7 != 0:
            print (i)
        else:
            print ("boom")
        i += 1

try_again()