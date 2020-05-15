def chech_guess(num):
    x = int(input("Enter a number from 1-100:\n"))
    if (x > num):
        print ("Too big!")
    elif (x < num):
        print("Too small!")
    else:
        print("You Won!")

chech_guess(55)