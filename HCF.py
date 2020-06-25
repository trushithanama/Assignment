#HCF
num1 = int(input("enter first vaule:"))
num2 = int(input("enter second value:"))
def compute_hcf(x,y):
    if x>y:
        smaller = y
    else:
         smaller = x
for i in range (1, smaller+1):
    if((x % 1 == 0) and (y % i == 0)):
         hcf = i
 return hcf 
 
 
print("the H.C.F. is" , compute_hcf(num1,num2))
        
