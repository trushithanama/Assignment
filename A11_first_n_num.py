#python program to read first n lines of a file
number_of_lines = int(input("enter no of lines to be printed: "))
a_file = open("file_name.txt")
for i in range(number_of_lines):
    line = a_file.readline()
    print(line)
    
    
    
    output
    enter no of lines to be printed: 2
Traceback (most recent call last):
  File "<string>", line 3, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'file_name.txt'
>>> 
