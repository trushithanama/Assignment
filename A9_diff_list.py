#python program to get the defference between the two lists

def Diff(li1, li2):
li_dif = [i for i in li1 + li2 if if i not in li1 or i not in li2]
    return li_dif

li1 = [10,15,20,25,30,35,40]
li2 = [25,40,35]
print(li3)


output
[10,15,20,30]


