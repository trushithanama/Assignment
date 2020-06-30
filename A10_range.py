#python program to check the number is in with in the range or not
def test_range (n) :
    if n in range(3,9):
        print( " %s is in the range"%str(n))
    else:
        print("the number is outside the given range.")
test_range(5)


output
5 is in the range
