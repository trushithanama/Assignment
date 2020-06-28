#python program to check a list is empty or not
list = input("enter list:")
def Enquiry(list):
    if len(list) == 0:
        return 0
    else:
        return 1
        
if Enquiry(list):
    print ("the list is not empty")
else:
    print("Empty List")
    
    
    
    
    output
    enter list:1,2,2
the list is not empty
>>> 
