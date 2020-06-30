#python funtion that accepts a string and calculates the number of upper case letters and lower case letters
def string_test (s) :
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
            d["UPPER_CASE"]+=1
        elif c.islower():
            d["LOWER_CASE"]+=1
        else:
            pass
    print("original string :", s)
    print("No. of upper case characters :", d["UPPER_CASE"])
    print("No. of lower case characters :", d["LOWER_CASE"])
    
string_test('the quick Brown Fox')


output
original string : the quick Brown Fox
No. of upper case characters : 2
No. of lower case characters : 14
>>> 
