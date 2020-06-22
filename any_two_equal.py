#any two are equal & all are equal
print("enter the first number")
first = input()
print("enter the second number")
second = input()
print("enter the third number")
third = input()
all = first == second and second == third and third == first
print("all numbers are equal",all)
any = first == second or second == third or third == first
print("any two numbers are equal",any)
