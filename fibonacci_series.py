#phython program to generate fibonacci series
n = int(input("enter the value of n: "))
a = 0
b = 1
sum = 0
count = 1
print("fibonacci series: ", end = " ")
while(count <=n) :
    print(sum, end = " ")
    count +=1
    a = b
    b = sum
    sum = a + b
    
    
    
    
    enter the value of n: 10
>>> 

fibonacci series:  0 1 1 2 3 5 8 13 21 34 >>> 
