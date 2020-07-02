#python program to find the sum of item in a list
def returnSum(myDict):
    
    
    sum = 0
    for i in myDict:
        sum = sum + myDict[i]
            
            
        return sum
        
dict = {'a': 100, 'b':200, 'c':300}
print("sum :", returnsum(dict))



output
600
