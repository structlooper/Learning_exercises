with open('html_file.html','r') as rf:
    with open('output.txt','w') as of:
        for string in rf.readlines():
            if "<a href=" in string :
                of.write(string) 


#Some Better Solution for video lecture no. 223