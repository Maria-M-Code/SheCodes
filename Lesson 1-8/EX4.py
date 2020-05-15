def chech_guess(num):
    x = int(input("Enter a number from 1-100:\n"))
    if (x > num):
        print ("Too big!")
    elif (x < num):
        print("Too small!")
    else:

        print("You Won!")
        return 0

def try_again(res):

    while chech_guess(res) != 0:
        # chech_guess(res)
        # try_again(res)
        if chech_guess(res) == 0:
            break

try_again(5)