#python program to read line by line and store in a list
def file_read(fname):
    with open(fname) as f :
        content_list = f.readlines()
        print(content_list)
        



output
number of lines = 6
