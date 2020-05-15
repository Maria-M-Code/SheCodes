

def try_again():
    i = 1

    y = 0
    while i <= 27:

        if y == 0:
            x = (input("Enter next number:\n"))
            if i % 7 != 0 and  int(x) == i:
                i += 1
                y = 1
                # print ("you win", i, x )
            elif i % 7 == 0 and str(x) == "boom":
                i += 1
                y = 1
                # print ("you win", i, x )
            else:
                print("you lose", i, x, i % 7)
                break
        if y == 1:
            if i % 7 != 0 :
                print (i)
                i += 1
                y = 0

            elif i % 7 == 0  :
                print ("boom")
                i += 1
                y = 0

                # print ("boom")
        # i += 1

try_again()