

def try_again():
    i = 1
    while i <= 27:
        x = (input("Enter next number:\n"))
        if i % 7 != 0 and  int(x) == i:
            i += 1
            # print ("you win", i, x )
        elif i % 7 == 0 and str(x) == "boom":
            i += 1
            # print ("you win", i, x )
        else:
            print("you lose", i, x, i % 7)
            break
            # print ("boom")
        # i += 1

try_again()