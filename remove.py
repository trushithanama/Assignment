# deleting a file from string

def remove(string,i)
    for j in range(len(string)):
        if j==i:
            string=string.replace(string[i], " ",1)
        return string
    if__name__=='__main__':
        string="python program"
        i=5
        print(remove(string,i))
        
        

        
