#python program to print a specified list after removing the 0th,4th,5th
color = ['red', 'green', 'white', 'black', 'pink', 'yellow']
color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)



output
['green', 'white', 'black']
>>> 
